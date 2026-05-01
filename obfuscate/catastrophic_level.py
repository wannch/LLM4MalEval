# pyminifier_api.py
"""
A small wrapper module that provides a programmatic API equivalent to:
    pyminifier -o obfu_pyminifier_5.py --bzip code.py

Features:
 - programmatic path (uses pyminifier.minification / pyminifier.obfuscate / pyminifier.compression if available)
 - fallback to subprocess calling `python -m pyminifier ...` if modules are not importable
 - simple CLI for convenience
"""

from __future__ import annotations
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

# ---------- Programmatic implementation (best-effort) ----------
def _programmatic_minify_obfuscate_and_pack(
    src_path: str,
    dest_path: str,
    compress: str = "bzip2",   # accepted: 'bzip2', 'gzip', 'lzma', 'zip' (pyz)
    obfuscate: bool = False,
    obfuscate_classes: bool = False,
    obfuscate_functions: bool = False,
    remove_docstrings: bool = True,
) -> str:
    """
    Try to use pyminifier's internal modules to minify/obfuscate/compress the file.
    Returns the path to the written output file on success.
    Raises ImportError if pyminifier modules are not available.
    """
    # Lazy import to allow fallback if not installed
    try:
        import pyminifier.minification as minification
        import pyminifier.obfuscate as obfuscate
        import pyminifier.compression as compression
    except Exception as e:
        raise ImportError("pyminifier modules not importable: " + str(e))

    src_path = Path(src_path)
    dest_path = Path(dest_path)

    if not src_path.exists():
        raise FileNotFoundError(f"Source file not found: {src_path}")

    source = src_path.read_text(encoding="utf-8")

    # Basic minification: dedent (this saves indentation bytes)
    try:
        source = minification.dedent(source, use_tabs=False)
    except Exception:
        # not fatal — keep original source if dedent fails
        pass

    # Optionally remove docstrings: pyminifier's CLI normally removes docstrings;
    # programmatic removal would require calling the same internals; many versions
    # implement docstring removal inside the main flow. We keep this minimal:
    if remove_docstrings:
        try:
            # there isn't a single public "remove_docstrings" in all versions;
            # many versions remove docstrings as part of other flows. We'll call
            # apply_obfuscation (which internally works on tokens) only if needed.
            # If a specific API exists in your installed version you can call it here.
            pass
        except Exception:
            pass

    # Obfuscate (if requested)
    if obfuscate:
        try:
            # apply_obfuscation expects source and returns obfuscated source
            source = obfuscate.apply_obfuscation(
                source,
                obfuscate_classes=obfuscate_classes,
                obfuscate_functions=obfuscate_functions,
            )
        except TypeError:
            # some versions take only (source,) signature
            source = obfuscate.apply_obfuscation(source)
        except Exception:
            # If obfuscation fails, raise so caller knows
            raise

    # Compression / self-extracting packing
    compress = (compress or "bzip2").lower()
    if compress in ("bzip2", "bz2", "bzip"):
        try:
            packed = compression.bz2_pack(source)
        except Exception as e:
            raise RuntimeError("bz2 packing failed: " + str(e))
    elif compress in ("gzip", "gz"):
        try:
            packed = compression.gz_pack(source)
        except Exception as e:
            raise RuntimeError("gzip packing failed: " + str(e))
    elif compress in ("lzma", "xz"):
        try:
            packed = compression.lzma_pack(source)
        except Exception as e:
            raise RuntimeError("lzma packing failed: " + str(e))
    elif compress in ("zip", "pyz", "zip_pack", "pyz_pack"):
        # zip_pack may require filepath and options; use zip_pack helper if available
        try:
            # zip_pack(filepath, options) returns a .pyz-like result or writes file.
            # We'll call zip_pack(filepath, options) if exposed; else fallback.
            if hasattr(compression, "zip_pack"):
                packed = compression.zip_pack(str(src_path), options=None)
            else:
                raise RuntimeError("zip_pack not available in this pyminifier build")
        except Exception as e:
            raise RuntimeError("zip/pyz packing failed: " + str(e))
    else:
        raise ValueError("Unknown compress option: " + str(compress))

    # Write packed text (it's text that includes the self-extracting stub)
    dest_path.write_text(packed, encoding="utf-8")
    return str(dest_path)


# ---------- CLI / subprocess fallback ----------
def _cli_call_pyminifier(
    src_path: str,
    dest_path: str,
    compress: str = "bzip2",
    extra_args: Optional[list[str]] = None,
) -> str:
    """
    Call pyminifier via subprocess: python -m pyminifier -o <dest> --bzip2 <src>
    This mirrors the exact CLI behavior and is robust when pyminifier isn't importable.
    """
    src_path = str(src_path)
    dest_path = str(dest_path)

    # map friendly compress name -> CLI flag
    compress_flag = {
        "bzip2": "--bzip2",
        "bz2": "--bzip2",
        "bzip": "--bzip2",
        "gzip": "--gzip",
        "gz": "--gzip",
        "lzma": "--lzma",
        "pyz": "--pyz",  # needs argument: --pyz=archive.pyz
    }.get(compress.lower(), "--bzip2")

    cmd = [sys.executable, "-m", "pyminifier", "-o", dest_path]
    if compress_flag.startswith("--pyz"):
        # if using --pyz you should supply archive name; we'll fallback to dest_path + .pyz
        # but original script used bzip so normal case won't hit here.
        cmd.append(f"--pyz={dest_path}.pyz")
    else:
        cmd.append(compress_flag)

    if extra_args:
        cmd.extend(extra_args)

    cmd.append(src_path)

    # run and raise on failure
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"pyminifier CLI failed (rc={proc.returncode}). stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
        )
    return dest_path


# ---------- Public wrapper function ----------
def pyminifier_api_minify(
    src_path: str,
    dest_path: str,
    compress: str = "bzip2",
    use_programmatic: bool = True,
    obfuscate: bool = False,
    obfuscate_classes: bool = False,
    obfuscate_functions: bool = False,
    extra_cli_args: Optional[list[str]] = None,
) -> str:
    """
    High-level wrapper:
     - tries programmatic call if use_programmatic True
     - falls back to CLI (python -m pyminifier ...) if programmatic fails

    Example (equivalent to your bash):
        pyminifier_api_minify("code.py", "obfu_pyminifier_5.py", compress="bzip2", use_programmatic=False)

    Returns the path to the produced file.
    """
    if use_programmatic:
        try:
            return _programmatic_minify_obfuscate_and_pack(
                src_path,
                dest_path,
                compress=compress,
                obfuscate=obfuscate,
                obfuscate_classes=obfuscate_classes,
                obfuscate_functions=obfuscate_functions,
            )
        except ImportError:
            # fall through to CLI fallback
            pass
        except Exception as e:
            # If programmatic failed in another way, surface debug info but try CLI fallback
            print(f"[pyminifier_api] programmatic attempt failed: {e!r}; falling back to CLI", file=sys.stderr)

    # CLI fallback
    return _cli_call_pyminifier(src_path, dest_path, compress=compress, extra_args=extra_cli_args)

import os, glob, random, shutil
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
                
                pyminifier_api_minify(
                    filepath,
                    dest_path=transformed_save_file,
                    compress=random.choice(['bzip2', 'gzip', 'lzma']),
                    use_programmatic=False,
                    obfuscate=True,
                    obfuscate_classes=True,
                    obfuscate_functions=True
                )

                # print(f"Transformed {filepath} successfully.")
            except Exception as e:
                print(f"Error in transformed code from {filepath}: {e}")
                shutil.copy(filepath, transformed_save_file)

# ---------- Simple CLI so you can call this module directly ----------
def _main():
    import argparse

    parser = argparse.ArgumentParser(prog="pyminifier_api", description="pyminifier wrapper (programmatic + CLI fallback)")
    parser.add_argument("src", help="source .py file to process")
    parser.add_argument("-o", "--outfile", default="obfu_pyminifier_5.py", help="output file")
    parser.add_argument("--compress", default="bzip2", choices=["bzip2", "gzip", "lzma", "pyz"], help="compression format")
    parser.add_argument("--no-programmatic", dest="programmatic", action="store_false", help="disable direct-import try; force CLI")
    parser.add_argument("--obfuscate", action="store_true", help="apply obfuscation (like -O)")
    parser.add_argument("--obf-classes", dest="obf_classes", action="store_true", help="obfuscate classes")
    parser.add_argument("--obf-funcs", dest="obf_funcs", action="store_true", help="obfuscate functions/methods")
    args = parser.parse_args()

    out = pyminifier_api_minify(
        args.src,
        dest_path=args.outfile,
        compress=args.compress,
        use_programmatic=args.programmatic,
        obfuscate=args.obfuscate,
        obfuscate_classes=args.obf_classes,
        obfuscate_functions=args.obf_funcs,
    )
    print("Wrote:", out)


# Obfuscate benign samples
def obfuscate_benign_samples(benign_dir:str, save_dir:str):

    for pyfile in glob.glob(f'{benign_dir}/*.py'):
        fn = os.path.basename(pyfile)

        try:
            transformed_save_file = os.path.join(save_dir, fn)

            pyminifier_api_minify(
                pyfile,
                dest_path=transformed_save_file,
                compress=random.choice(['bzip2', 'gzip', 'lzma']),
                use_programmatic=False,
                obfuscate=True,
                obfuscate_classes=True,
                obfuscate_functions=True
            )

        except Exception as e:
            print(f"Error in transformed code from {pyfile}: {e}")
            continue
        

if __name__ == "__main__":
    # _main()

    obfuscate_malicious_samples(
        'malicious_packages_benchmark/malicious_code_384_by_category',
        'malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/catastrophic_level'
    )
    
    obfuscate_benign_samples(
        'malicious_packages_benchmark/benign_65',
        'malicious_packages_benchmark/benign_65_obfuscated/catastrophic_level'
    )