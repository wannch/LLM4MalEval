"""
py_transformer_module.py

A conservative Python source-to-source transformer that supports:
 1) Swapping adjacent statements when it is safe (no read/write conflicts and no calls/attributes).
 2) Inserting dead/garbage code (wrapped under `if False:`) between statements.

Notes:
 - This tool uses a conservative static analysis based on AST name reads/writes and presence of Calls/Attributes.
 - It is intentionally conservative: it avoids swapping statements that contain function calls, attribute/subscript access,
   or any potential side-effects it cannot prove safe.
 - Requires Python 3.9+ for ast.unparse. If running on older Python, install `astor` and set `USE_ASTOR = True`.

API:
 - transform_source(src, swap=True, swap_prob=1.0, insert_dead=True, dead_density=0.2, seed=None)
 - transform_file(path, outpath, ...)

This is a best-effort educational tool. Test transformed code thoroughly.
"""

from __future__ import annotations
import ast
import random
import itertools
import sys
from typing import Tuple, Set

USE_ASTOR = False
try:
    from ast import unparse as ast_unparse
except Exception:
    try:
        import astor
        ast_unparse = astor.to_source
        USE_ASTOR = True
    except Exception:
        raise RuntimeError("Requires Python 3.9+ or astor installed for code generation")


class ReadWriteAnalyzer(ast.NodeVisitor):
    """Collect conservative sets of names read and written by a statement.
    Also detects presence of Calls, Attributes or Subscripts which indicate potential side-effects.
    """

    def __init__(self):
        self.reads: Set[str] = set()
        self.writes: Set[str] = set()
        self.has_call = False
        self.has_attribute_or_subscript = False

    def visit_Name(self, node: ast.Name):
        if isinstance(node.ctx, ast.Store):
            self.writes.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.reads.add(node.id)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        self.has_call = True
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        # attribute accesses may involve side-effects (property, descriptors) or aliasing
        self.has_attribute_or_subscript = True
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript):
        # subscripts may have side-effects via __getitem__ / __setitem__
        self.has_attribute_or_subscript = True
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        # target of AugAssign is both read and written
        self._collect_names_in_target(node.target, stores=True, loads=True)
        self.visit(node.value)

    def visit_Assign(self, node: ast.Assign):
        for t in node.targets:
            self._collect_names_in_target(t, stores=True)
        self.visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign):
        if node.target is not None:
            self._collect_names_in_target(node.target, stores=True)
        if node.value is not None:
            self.visit(node.value)

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            name = alias.asname or alias.name.split(".")[0]
            self.writes.add(name)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        for alias in node.names:
            if alias.name == '*':
                # this is a wildcard import; be conservative
                self.has_attribute_or_subscript = True
            else:
                name = alias.asname or alias.name
                self.writes.add(name)

    def generic_visit(self, node):
        super().generic_visit(node)

    def _collect_names_in_target(self, node, stores=False, loads=False):
        for n in ast.walk(node):
            if isinstance(n, ast.Name):
                if isinstance(n.ctx, ast.Store) or stores:
                    self.writes.add(n.id)
                if isinstance(n.ctx, ast.Load) or loads:
                    self.reads.add(n.id)


def analyze_stmt(stmt: ast.stmt) -> ReadWriteAnalyzer:
    a = ReadWriteAnalyzer()
    a.visit(stmt)
    return a


def can_swap(stmt1: ast.stmt, stmt2: ast.stmt) -> bool:
    """Conservative check whether two adjacent statements can be swapped.

    Conditions used:
      - No write->read or write->write conflicts in either direction.
      - Neither statement contains a Call or attribute/subscript access (conservative side-effects).
      - Only consider swapping for "simple" top-level statements (Assign, AnnAssign, Expr, Import, ImportFrom, Pass).
    """

    simple_allowed = (ast.Assign, ast.AnnAssign, ast.Expr, ast.Pass, ast.Import, ast.ImportFrom)
    if not isinstance(stmt1, simple_allowed) or not isinstance(stmt2, simple_allowed):
        return False

    a1 = analyze_stmt(stmt1)
    a2 = analyze_stmt(stmt2)

    # conservative: if either has call/attribute/subscript, don't swap
    if a1.has_call or a2.has_call or a1.has_attribute_or_subscript or a2.has_attribute_or_subscript:
        return False

    # If stmt1 writes something that stmt2 reads or writes, swapping can change behavior
    if a1.writes & (a2.reads | a2.writes):
        return False
    # If stmt2 writes something that stmt1 reads or writes, swapping can change behavior
    if a2.writes & (a1.reads | a1.writes):
        return False

    # otherwise, conservative-allow
    return True


_counter = itertools.count(1)


def make_dead_block(num_stmts=2) -> ast.If:
    """Create a dead code block: if False: <some harmless statements>

    The statements are simple assignments and a nested function definition to avoid accidental execution.
    """
    dead_name_base = f"_var_{next(_counter)}"
    stmts = []
    for i in range(num_stmts):
        name = f"{dead_name_base}_{i}"
        # assign a literal (tuple of numbers) so it doesn't rely on external names
        assign = ast.Assign(
            targets=[ast.Name(id=name, ctx=ast.Store())],
            value=ast.Tuple(elts=[ast.Constant(value=random.randint(0, 1000)) for _ in range(3)], ctx=ast.Load()),
        )
        stmts.append(assign)

    # add a dummy function definition inside dead block
    fn_name = f"{dead_name_base}_fn"
    fn = ast.FunctionDef(
        name=fn_name,
        args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]),
        body=[ast.Pass()],
        decorator_list=[],
    )
    stmts.append(fn)

    dead_if = ast.If(test=ast.Constant(value=False), body=stmts, orelse=[])
    ast.fix_missing_locations(dead_if)
    return dead_if


def swap_adjacent_in_body(body: list[ast.stmt], swap_prob=1.0, rng: random.Random | None = None) -> list[ast.stmt]:
    if rng is None:
        rng = random
    i = 0
    out = list(body)
    # iterate and attempt swap for adjacent pairs
    while i < len(out) - 1:
        s1 = out[i]
        s2 = out[i + 1]
        if rng.random() <= swap_prob and can_swap(s1, s2):
            out[i], out[i + 1] = s2, s1
            # skip past the swapped pair to avoid re-swapping reversed
            i += 2
        else:
            i += 1
    return out


def insert_dead_code_in_body(body: list[ast.stmt], density=0.2, rng: random.Random | None = None) -> list[ast.stmt]:
    """Insert dead code blocks between statements with given density (fraction of possible insertion points).

    density: float in [0,1]. For each gap between statements we insert with probability density.
    """
    if rng is None:
        rng = random
    out: list[ast.stmt] = []
    for idx, stmt in enumerate(body):
        out.append(stmt)
        # don't insert after the last stmt necessarily (but it's allowed)
        if rng.random() < density:
            dead = make_dead_block(num_stmts=rng.randint(1, 3))
            out.append(dead)
    return out


def transform_ast(tree: ast.AST, swap=True, swap_prob=1.0, insert_dead=True, dead_density=0.2, seed=None) -> ast.AST:
    rng = random.Random(seed)

    class Transformer(ast.NodeTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
            self.generic_visit(node)
            node.body = transform_stmt_list(node.body)
            return node

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
            self.generic_visit(node)
            node.body = transform_stmt_list(node.body)
            return node

        def visit_Module(self, node: ast.Module) -> ast.AST:
            self.generic_visit(node)
            node.body = transform_stmt_list(node.body)
            return node

    def transform_stmt_list(stmt_list: list[ast.stmt], recursive:bool = False) -> list[ast.stmt]:
        new_list = list(stmt_list)
        if swap:
            new_list = swap_adjacent_in_body(new_list, swap_prob=swap_prob, rng=rng)
        if insert_dead:
            new_list = insert_dead_code_in_body(new_list, density=dead_density, rng=rng)

        if recursive:
            # recursively apply to inner bodies (for e.g. if/for/while)
            # but keep the conservative policy: transform bodies inside compound statements
            for s in new_list:
                # handle compound statements: If, For, While, With, Try
                if isinstance(s, ast.If):
                    s.body = transform_stmt_list(s.body)
                    s.orelse = transform_stmt_list(s.orelse)
                elif isinstance(s, (ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith)):
                    if hasattr(s, 'body'):
                        s.body = transform_stmt_list(s.body)
                    if hasattr(s, 'orelse'):
                        s.orelse = transform_stmt_list(s.orelse)
                elif isinstance(s, ast.Try):
                    s.body = transform_stmt_list(s.body)
                    s.orelse = transform_stmt_list(s.orelse)
                    s.finalbody = transform_stmt_list(s.finalbody)
                    for h in s.handlers:
                        h.body = transform_stmt_list(h.body)
        return new_list

    transformer = Transformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    return new_tree


def transform_source(src: str, *, swap=True, swap_prob=1.0, insert_dead=True, dead_density=0.2, seed=None) -> str:
    tree = ast.parse(src)
    new_tree = transform_ast(tree, swap=swap, swap_prob=swap_prob, insert_dead=insert_dead, dead_density=dead_density, seed=seed)
    return ast_unparse(new_tree)


def transform_file(path: str, outpath: str | None = None, **kwargs) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    new_src = transform_source(src, **kwargs)
    if outpath is None:
        outpath = path + '.transformed.py'
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(new_src)
    return outpath

import os, glob
# Obfuscate malicious package samples
def obfuscate_malicious_samples(malicious_samples_dir: str, save_transformed: str):
    for txtfile in glob.glob(f'{malicious_samples_dir}/*.txt'):
        with open(txtfile, 'r') as f:
            filenames = f.read()

        cate = os.path.basename(txtfile).removesuffix('.txt')
        
        for fn in filenames.splitlines():
            filepath = os.path.join(malicious_samples_dir, cate, fn)

            try:
                os.makedirs(os.path.join(save_transformed, cate), exist_ok=True)
                
                transformed_save_file = os.path.join(save_transformed, cate, fn)
                
                transform_file(filepath, transformed_save_file)

                # print(f"Transformed {filepath} successfully.")
            except Exception as e:
                print(f"Error in transformed code from {filepath}: {e}")

# Obfuscate benign samples
def obfuscate_benign_samples(benign_dir:str, save_dir:str):

    for pyfile in glob.glob(f'{benign_dir}/*.py'):
        fn = os.path.basename(pyfile)

        try:
            transformed_save_file = os.path.join(save_dir, fn)
            transform_file(pyfile, transformed_save_file)        

        except Exception as e:
            print(f"Error in transformed code from {pyfile}: {e}")
            continue


def main():
    import argparse

    p = argparse.ArgumentParser(description='Conservative Python statement-swapping + dead-code inserter')
    p.add_argument('src', help='source file to transform')
    p.add_argument('-o', '--out', help='output path (default: src.transformed.py)')
    p.add_argument('--no-swap', dest='swap', action='store_false')
    p.add_argument('--swap-prob', type=float, default=1.0)
    p.add_argument('--no-dead', dest='insert_dead', action='store_false')
    p.add_argument('--dead-density', type=float, default=0.20)
    p.add_argument('--seed', type=int, default=None)
    args = p.parse_args()

    out = transform_file(args.src, args.out, swap=args.swap, swap_prob=args.swap_prob, insert_dead=args.insert_dead, dead_density=args.dead_density, seed=args.seed)
    print(f'Transformed file written to: {out}')

if __name__ == '__main__':
    # main()
    
    obfuscate_malicious_samples(
        'malicious_packages_benchmark/malicious_code_384_by_category',
        'malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/structure_level'
    )

    obfuscate_benign_samples(
        'malicious_packages_benchmark/benign_65',
        'malicious_packages_benchmark/benign_65_obfuscated/structure_level'
    )