"""
injector_ast.py

AST-based injector that ensures syntactically-correct output after injection.
Requires Python 3.9+ (for ast.unparse).

Usage examples:
  python injector_ast.py --b good.py --m malicious.py --out good_injected.py --mode 1
  python injector_ast.py --b good.py --m_dir malwares/ --out_dir injected/ --mode 6 --seed 42
"""

import ast
import os
import random
import argparse
import sys
from typing import List, Optional

if sys.version_info < (3, 9):
    raise RuntimeError("This script requires Python 3.9+ (for ast.unparse).")

class ASTInjector:
    def __init__(self, seed: Optional[int] = None):
        if seed is not None:
            random.seed(seed)

    # ---------- parsing helpers ----------
    @staticmethod
    def read_text(path: str) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def parse_module(text: str) -> ast.Module:
        return ast.parse(text)

    @staticmethod
    def module_top_nodes(mod: ast.Module) -> List[ast.stmt]:
        # Return top-level statements as list
        return list(mod.body)

    @staticmethod
    def remove_module_docstring_nodes(nodes: List[ast.stmt]) -> List[ast.stmt]:
        # If first node is a module docstring (Expr(Constant/Str)), drop it.
        if nodes and isinstance(nodes[0], ast.Expr) and isinstance(nodes[0].value, (ast.Constant, ast.Str)) and isinstance(nodes[0].value.value, str):
            return nodes[1:]
        return nodes

    # ---------- AST insertion implementations ----------
    def inject_mode_1_head(self, m_nodes: List[ast.stmt], b_nodes: List[ast.stmt]) -> ast.Module:
        new_body = m_nodes + b_nodes
        return ast.Module(body=new_body, type_ignores=[])

    def inject_mode_2_middle(self, m_nodes: List[ast.stmt], b_nodes: List[ast.stmt]) -> ast.Module:
        mid = (len(b_nodes) // 2)
        new_body = b_nodes[:mid] + m_nodes + b_nodes[mid:]
        return ast.Module(body=new_body, type_ignores=[])

    def inject_mode_3_tail(self, m_nodes: List[ast.stmt], b_nodes: List[ast.stmt]) -> ast.Module:
        new_body = b_nodes + m_nodes
        return ast.Module(body=new_body, type_ignores=[])

    def inject_mode_4_into_function(self, m_nodes: List[ast.stmt], b_mod: ast.Module) -> ast.Module:
        b_nodes = list(b_mod.body)
        funcs_idx = [i for i, n in enumerate(b_nodes) if isinstance(n, ast.FunctionDef)]
        if not funcs_idx:
            # fallback to tail
            return self.inject_mode_3_tail(m_nodes, b_nodes)
        idx = random.choice(funcs_idx)
        func = b_nodes[idx]
        # insert at start of function body
        func.body = m_nodes + func.body
        b_nodes[idx] = func
        return ast.Module(body=b_nodes, type_ignores=[])

    def inject_mode_5_into_class_method(self, m_nodes: List[ast.stmt], b_mod: ast.Module) -> ast.Module:
        b_nodes = list(b_mod.body)
        classes_idx = [i for i, n in enumerate(b_nodes) if isinstance(n, ast.ClassDef)]
        # collect class methods
        candidate = None
        for ci in classes_idx:
            cls = b_nodes[ci]
            methods = [m for m in cls.body if isinstance(m, ast.FunctionDef)]
            if methods:
                candidate = (ci, methods)
                break
        if not candidate:
            # fallback to function insertion
            return self.inject_mode_4_into_function(m_nodes, b_mod)
        ci, methods = candidate
        chosen_method = random.choice(methods)
        # insert at start of method body
        chosen_method.body = m_nodes + chosen_method.body
        # replace method in class body
        new_cls_body = []
        for item in b_nodes[ci].body:
            if item is chosen_method:
                new_cls_body.append(chosen_method)
            else:
                new_cls_body.append(item)
        b_nodes[ci].body = new_cls_body
        return ast.Module(body=b_nodes, type_ignores=[])

    def inject_mode_6_split_to_global(self, m_nodes: List[ast.stmt], b_mod: ast.Module) -> ast.Module:
        b_nodes = list(b_mod.body)
        # we preserve order of m_nodes but randomly choose slots
        slots = len(b_nodes) + 1
        # choose nondecreasing slot indices to preserve order; use random.choices then sort
        chosen_slots = sorted(random.choices(range(slots), k=len(m_nodes)))
        inserts_by_slot = {}
        for node, slot in zip(m_nodes, chosen_slots):
            inserts_by_slot.setdefault(slot, []).append(node)
        new_body = []
        for slot in range(slots):
            # add original node for slot>0
            if slot > 0:
                new_body.append(b_nodes[slot - 1])
            # add inserted nodes for this slot
            for n in inserts_by_slot.get(slot, []):
                new_body.append(n)
        return ast.Module(body=new_body, type_ignores=[])

    def inject_mode_7_split_into_function(self, m_nodes: List[ast.stmt], b_mod: ast.Module) -> ast.Module:
        b_nodes = list(b_mod.body)
        funcs_idx = [i for i, n in enumerate(b_nodes) if isinstance(n, ast.FunctionDef)]
        if not funcs_idx:
            # fallback to global
            return self.inject_mode_6_split_to_global(m_nodes, b_mod)
        idx = random.choice(funcs_idx)
        func = b_nodes[idx]
        # decide slots in function body
        slots = len(func.body) + 1
        chosen_slots = sorted(random.choices(range(slots), k=len(m_nodes)))
        inserts_by_slot = {}
        for node, slot in zip(m_nodes, chosen_slots):
            inserts_by_slot.setdefault(slot, []).append(node)
        new_func_body = []
        for slot in range(slots):
            if slot > 0:
                new_func_body.append(func.body[slot - 1])
            for n in inserts_by_slot.get(slot, []):
                new_func_body.append(n)
        func.body = new_func_body
        b_nodes[idx] = func
        return ast.Module(body=b_nodes, type_ignores=[])

    # ---------- public API ----------
    def inject(self, m_text: str, b_text: str, mode: int) -> str:
        # parse modules
        m_mod = self.parse_module(m_text)
        b_mod = self.parse_module(b_text)

        # extract top-level nodes; remove module docstring from M (as requested)
        m_nodes = self.remove_module_docstring_nodes(self.module_top_nodes(m_mod))
        b_nodes = self.module_top_nodes(b_mod)

        # choose injection mode
        if mode == 1:
            new_mod = self.inject_mode_1_head(m_nodes, b_nodes)
        elif mode == 2:
            new_mod = self.inject_mode_2_middle(m_nodes, b_nodes)
        elif mode == 3:
            new_mod = self.inject_mode_3_tail(m_nodes, b_nodes)
        elif mode == 4:
            new_mod = self.inject_mode_4_into_function(m_nodes, b_mod)
        elif mode == 5:
            new_mod = self.inject_mode_5_into_class_method(m_nodes, b_mod)
        elif mode == 6:
            new_mod = self.inject_mode_6_split_to_global(m_nodes, b_mod)
        elif mode == 7:
            new_mod = self.inject_mode_7_split_into_function(m_nodes, b_mod)
        else:
            raise ValueError("mode must be 1..7")

        # fix locations and unparse
        ast.fix_missing_locations(new_mod)
        code = ast.unparse(new_mod)

        # final syntax check (should pass because we built valid AST, but check anyway)
        try:
            ast.parse(code)
        except Exception as e:
            # This should be rare; provide debug info
            raise RuntimeError(f"Generated code failed Python parse check: {e}")

        return code

    def inject_file_pair(self, m_path: str, b_path: str, mode: int, out_path: str) -> None:
        m_text = self.read_text(m_path)
        b_text = self.read_text(b_path)
        new_code = self.inject(m_text, b_text, mode)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(new_code)

    def batch_inject(self, m_dir: str, b_path: str, out_dir: str, mode: int, pattern_ext: str = ".py") -> None:
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        for fname in os.listdir(m_dir):
            if not fname.endswith(pattern_ext):
                continue
            m_path = os.path.join(m_dir, fname)
            base_bname = os.path.splitext(os.path.basename(b_path))[0]
            base_mname = os.path.splitext(fname)[0]
            out_name = f"{base_bname}__with__{base_mname}__mode{mode}.py"
            out_path = os.path.join(out_dir, out_name)
            try:
                self.inject_file_pair(m_path, b_path, mode, out_path)
                print(f"Injected {m_path} -> {out_path}")
            except Exception as e:
                print(f"Failed to inject {m_path}: {e}")

# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="AST-based injector (ensures syntax correctness).")
    parser.add_argument('--b', required=True, help="path to benign module B (single file)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--m', help="path to malicious module M (single file)")
    group.add_argument('--m_dir', help="directory containing multiple malicious modules (batch mode)")
    parser.add_argument('--out', help="output file path (single mode) or output directory (batch mode)", required=True)
    parser.add_argument('--mode', type=int, choices=list(range(1,8)), required=True, help="injection mode 1..7")
    parser.add_argument('--seed', type=int, default=None, help="random seed")
    args = parser.parse_args()

    inj = ASTInjector(seed=args.seed)
    if args.m:
        inj.inject_file_pair(args.m, args.b, args.mode, args.out)
        print(f"Wrote injected file to {args.out}")
    else:
        inj.batch_inject(args.m_dir, args.b, args.out, args.mode)

if __name__ == '__main__':
    main()
