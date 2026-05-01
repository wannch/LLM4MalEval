# code_transformer.py
import os
import io
import keyword
import tokenize
import token as token_module
import math
import glob
from typing import List, Tuple


class TransformError(Exception):
    pass


class CodeTransformer:
    """
    Transform Python source code with the following operations:
      1. remove all comments
      2. remove all blank lines
      3. change indentation to a specified number of spaces per indent level
      4. minimize spacing between tokens while preserving syntax (keeps
         necessary spaces like 'def func', prevents merging identifiers)
    """

    def __init__(self, indent_spaces: int = 4):
        if indent_spaces < 0:
            raise ValueError("indent_spaces must be non-negative")
        self.indent_spaces = indent_spaces

    def _gcd_of_list(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        if not nums:
            return 0
        g = nums[0]
        for n in nums[1:]:
            g = math.gcd(g, n)
        return g
    
    def _count_leading_space(self, code_line:str) -> int:
        for i in range(len(code_line)):
            if code_line[i] not in (' ', '\t'):
                return i

    def transform(self, source: str) -> str:
        """
        Transform source code and return transformed code string.
        Raises SyntaxError if the transformed code is not valid Python.
        """
        
        tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))

        # Collect INDENT lengths (after expandtabs) to infer indentation unit
        indent_len = 0
        for tok in tokens:
            tok_type, tok_str, _, _, _ = tok
            
            if tok_type == token_module.INDENT:
                indent_len = len(tok_str)
                break

        # print(f"Detected indent length: {indent_len}")
        nu_2_line = {i:line for i, line in enumerate(source.splitlines(), start=1)}
        
        # Build a list of tokens to keep (skip COMMENT and NL)
        kept_tokens: List[Tuple[int, str]] = []  # (type, string)
        for i, tok in enumerate(tokens):
            tok_type, tok_str, _, _, _ = tok

            if tok_type == token_module.STRING:
                if i > 0:
                    prev_type, prev_str, _, _, _ = tokens[i - 1]
                    if prev_type == token_module.INDENT or prev_type == token_module.NEWLINE:
                        continue
            if tok_type == token_module.COMMENT:
                continue  # remove all comments
            if tok_type == token_module.NL:
                # NL = non-significant newline (e.g. inside multi-line constructs)
                # we drop NL to remove blank/extra lines; keep NEWLINE (logical)
                continue
            # if tok_type == token_module.INDENT:
            #     # compute indent level and replace with requested spaces
            #     # count expanded length, divide by unit -> level
            #     orig_len = len(tok_str.expandtabs(8))
            #     level = orig_len // unit if unit else 0
            #     new_indent = " " * (self.indent_spaces * level)
            #     print(level, len(new_indent))
            #     kept_tokens.append((token_module.INDENT, new_indent))
            #     continue
            if tok_type == token_module.DEDENT:
                kept_tokens.append(tok)
                continue
            # For all other tokens, keep their string (strings are significant)
            kept_tokens.append(tok)

        # Now stitch tokens into a source string with minimal spacing but
        # preserving syntax. We'll use a conservative rule:
        # Insert a single space between tokens if both sides are identifier/number-like
        # or keywords, because joining them would create a different token.
        out_parts: List[str] = []
        prev_type = None
        prev_str = ""
        seen_lines = set()
        # Process left tokens
        for tok in kept_tokens:
            tok_type, tok_str, start, end, line = tok
            row, col = start

            if tok_type != token_module.DEDENT and tok_type != token_module.ENDMARKER and row not in seen_lines:
                ct = self._count_leading_space(nu_2_line[row])
                ct //= indent_len if indent_len > 0 else 1
                out_parts.append(" " * (self.indent_spaces * ct))
                seen_lines.add(row)

            # Skip zero-length tokens
            if tok_str == "" or tok_type == token_module.INDENT:
                continue

            need_space = False
            # If previous exists, decide if space required
            if prev_type is not None:
                # If both sides are NAME/NUMBER/keyword, need space.
                left_is_name_num_kw = (
                    prev_type == token_module.NAME
                    or prev_type == token_module.NUMBER
                    or (prev_type == token_module.OP and prev_str == "@")  # decorator edge-case handled below
                )
                right_is_name_num_kw = (
                    tok_type == token_module.NAME
                    or tok_type == token_module.NUMBER
                )
                # keyword detection: keywords are token.NAME but require separation
                left_is_kw = (prev_type == token_module.NAME and keyword.iskeyword(prev_str))
                right_is_kw = (tok_type == token_module.NAME and keyword.iskeyword(tok_str))

                if (left_is_name_num_kw or left_is_kw) and (right_is_name_num_kw or right_is_kw):
                    need_space = True

                # Additional conservative cases:
                # - If previous token is a string literal and next is NAME/NUMBER it's safer to have a space
                if prev_type == token_module.STRING and (tok_type in (token_module.NAME, token_module.NUMBER)):
                    need_space = True
                if tok_type == token_module.STRING and (prev_type in (token_module.NAME, token_module.NUMBER)):
                    need_space = True

                # Ensure 'def'/'class' (keywords) keep a space before the NAME that follows:
                if (prev_type == token_module.NAME and keyword.iskeyword(prev_str)) and tok_type == token_module.NAME:
                    need_space = True

                # Avoid merging two operators/ punctuations that would produce another operator,
                # but this is usually fine without spaces; we keep no-space by default.

            if need_space:
                out_parts.append(" ")
            out_parts.append(tok_str)

            prev_type = tok_type
            prev_str = tok_str

        out = "".join(out_parts)

        # Remove wholly empty lines (lines that contain only whitespace)
        # but preserve meaningful NEWLINEs (we kept logical NEWLINE as token '\n' in sequence).
        lines = out.splitlines()
        filtered_lines = [ln for ln in lines if ln.strip() != ""]
        out2 = "\n".join(filtered_lines) + ("\n" if out and not out.endswith("\n") else "")

        # Final syntax check
        try:
            compile(out2, "<transformed>", "exec")
        except SyntaxError as e:
            # For debugging, include helpful message
            raise SyntaxError(f"Transformed code is not syntactically valid: {e.msg} (line {e.lineno})") from e

        return out2

# Obfuscate malicious package samples
def obfuscate_malicious_samples(malicious_samples_dir: str, save_transformed: str):
    ct = CodeTransformer(indent_spaces=2)
    for txtfile in glob.glob(f'{malicious_samples_dir}/*.txt'):
        with open(txtfile, 'r') as f:
            filenames = f.read()

        cate = os.path.basename(txtfile).removesuffix('.txt')
        
        for fn in filenames.splitlines():
            filepath = os.path.join(malicious_samples_dir, cate, fn)

            with open(filepath, 'r') as f:
                code = f.read()

            try:
                transformed = ct.transform(code)
                os.makedirs(os.path.join(save_transformed, cate), exist_ok=True)
                
                print(os.path.join(save_transformed, cate, fn))
                with open(os.path.join(save_transformed, cate, fn), 'w') as f:
                    f.write(transformed)

                print(f"Transformed {filepath} successfully.")
            except SyntaxError as e:
                print(f"Syntax error in transformed code from {txtfile}: {e}")

# Obfuscate benign samples
def obfuscate_benign_samples(benign_dir:str, save_dir:str):
    ct = CodeTransformer(indent_spaces=2)

    for pyfile in glob.glob(f'{benign_dir}/*.py'):
        with open(pyfile, 'r') as f:
            code = f.read()
        fn = os.path.basename(pyfile)

        try:
            transformed = ct.transform(code)
            with open(os.path.join(save_dir, fn), 'w') as f:
                f.write(transformed)

        except SyntaxError as e:
            print(f"Syntax error in transformed code from {pyfile}: {e}")
            continue
        

if __name__ == "__main__":
    obfuscate_malicious_samples('malicious_packages_benchmark/malicious_code_384_by_category',
                               'malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/layout_level')    

    obfuscate_benign_samples(
        'malicious_packages_benchmark/benign_65',
        'malicious_packages_benchmark/benign_65_obfuscated/layout_level'
    )