import glob
import os
import traceback
from types import SimpleNamespace
import ast
import tokenize
from typing import Optional
import pyminifier.obfuscate as pm_obf
import pyminifier.token_utils as token_utils


class PyMinifierObfuscator:
    def __init__(
        self,
        replacement_length: int = 1,
        use_nonlatin: bool = False,
        obfuscate_all: bool = True,
        obf_classes: bool = True,
        obf_functions: bool = True,
        obf_variables: bool = True,
        obf_import_methods: bool = True,
        obf_builtins: bool = False,
    ):
        self.opt = SimpleNamespace(
            replacement_length=str(replacement_length),
            use_nonlatin=use_nonlatin,
            obfuscate=obfuscate_all,
            obf_classes=obf_classes,
            obf_functions=obf_functions,
            obf_variables=obf_variables,
            obf_import_methods=obf_import_methods,
            obf_builtins=obf_builtins,
        )
        self.name_generator = pm_obf.obfuscation_machine(
            identifier_length=int(self.opt.replacement_length),
            use_unicode=use_nonlatin if hasattr(pm_obf, "obfuscation_machine") else False
        )

    def obfuscate_identifiers(self, source: str, module_name: str = "__main__") -> str:
        tokens = token_utils.listified_tokenizer(source)

        pm_obf.obfuscate(
            module_name,
            tokens,
            self.opt,
            name_generator=self.name_generator,
            table=None,
        )

        return token_utils.untokenize(tokens)

    def _build_string_expr(self, s: str) -> str:
        if s == "":
            return "''"
        parts = ",".join(f"chr({ord(ch)})" for ch in s)
        return '("".join([%s]))' % parts

    def _build_number_expr(self, n_text: str) -> str:
        try:
            _ = int(n_text, 0)
            digits = list(n_text)
            seq = ",".join(f"chr({ord(ch)})" for ch in n_text)
            return f'int("".join([{seq}]))'
        except Exception:
            try:
                _ = float(n_text)
                seq = ",".join(f"chr({ord(ch)})" for ch in n_text)
                return f'float("".join([{seq}]))'
            except Exception:
                return n_text

    def obfuscate_constants(self, source: str) -> str:
        tokens = token_utils.listified_tokenizer(source)

        i = 0
        while i < len(tokens):
            tok = tokens[i]
            tok_type, tok_str = tok[0], tok[1]

            if tok_type == tokenize.STRING:
                prefix = ""
                lower = tok_str.lstrip()
                first_quote_idx = None
                for idx, ch in enumerate(lower):
                    if ch in ("'", '"'):
                        first_quote_idx = idx
                        break
                if first_quote_idx is None:
                    i += 1
                    continue
                prefix = lower[:first_quote_idx]
                if 'f' in prefix.lower() or 'F' in prefix or 'b' in prefix.lower():
                    i += 1
                    continue
                try:
                    value = ast.literal_eval(tok_str)
                    if isinstance(value, str):
                        expr = self._build_string_expr(value)
                        new_tokens = token_utils.listified_tokenizer(expr)
                        tokens[i:i+1] = new_tokens
                        i += len(new_tokens)
                        continue
                except Exception:
                    i += 1
                    continue

            if tok_type == tokenize.NUMBER:
                try:
                    expr = self._build_number_expr(tok_str)
                    new_tokens = token_utils.listified_tokenizer(expr)
                    tokens[i:i+1] = new_tokens
                    i += len(new_tokens)
                    continue
                except Exception:
                    i += 1
                    continue

            i += 1

        return token_utils.untokenize(tokens)

    def obfuscate(self, source: str, module_name: str = "__main__") -> str:
        
        after_id = self.obfuscate_identifiers(source, module_name=module_name)
        try:
            after_consts = self.obfuscate_constants(after_id)
        except Exception:
            return source

        return after_consts


def obfuscate_malicious_samples(malicious_samples_dir: str, save_transformed: str):
    ob = PyMinifierObfuscator(replacement_length=1, use_nonlatin=False)
    for txtfile in glob.glob(f'{malicious_samples_dir}/*.txt'):
        with open(txtfile, 'r') as f:
            filenames = f.read()

        cate = os.path.basename(txtfile).removesuffix('.txt')
        
        for fn in filenames.splitlines():
            filepath = os.path.join(malicious_samples_dir, cate, fn)

            with open(filepath, 'r') as f:
                code = f.read()
            
            try:
                transformed = ob.obfuscate(code)
                
                os.makedirs(os.path.join(save_transformed, cate), exist_ok=True)
                with open(os.path.join(save_transformed, cate, fn), 'w') as f:
                    f.write(transformed)

                # print(f"Transformed {filepath} successfully.")
            except Exception as e:
                traceback.print_exc()
                print(f"Error in transforming code from {filepath}")

def obfuscate_layout_level_samples(layout_level_dir:str, save_transformed:str):
    ob = PyMinifierObfuscator(replacement_length=1, use_nonlatin=False)
    
    for cate_dir in os.listdir(layout_level_dir):
        cate_path = os.path.join(layout_level_dir, cate_dir)

        for fn in os.listdir(cate_path):
            if not fn.endswith('.py'):
                continue
            filepath = os.path.join(cate_path, fn)

            with open(filepath, 'r') as f:
                code = f.read()
            
            try:
                transformed = ob.obfuscate(code)
                
                os.makedirs(os.path.join(save_transformed, cate_dir), exist_ok=True)
                with open(os.path.join(save_transformed, cate_dir, fn), 'w') as f:
                    f.write(transformed)

                # print(f"Transformed {filepath} successfully.")
            except Exception as e:
                traceback.print_exc()
                print(f"Error in transforming code from {filepath}")

# Obfuscate benign samples
def obfuscate_benign_samples(benign_dir:str, save_dir:str):
    ob = PyMinifierObfuscator(replacement_length=1, use_nonlatin=False)

    for pyfile in glob.glob(f'{benign_dir}/*.py'):
        with open(pyfile, 'r') as f:
            code = f.read()
        fn = os.path.basename(pyfile)

        try:
            transformed = ob.obfuscate(code)
            with open(os.path.join(save_dir, fn), 'w') as f:
                f.write(transformed)

        except Exception as e:
            print(f"Error in transformed code from {pyfile}: {e}")
            continue
        

if __name__ == "__main__":

    obfuscate_malicious_samples(
        'malicious_packages_benchmark/malicious_code_384_by_category',
        'malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/word_level'
    )

    obfuscate_benign_samples(
        'malicious_packages_benchmark/benign_65',
        'malicious_packages_benchmark/benign_65_obfuscated/word_level'
    )