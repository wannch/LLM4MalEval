# AST-Based Code Injection

This directory contains scripts for injecting Python code from one module into another while keeping the generated output syntactically valid.

## Files

- `injector.py`: the main AST-based Python injector.
- `run_injector.sh`: a batch runner that executes `injector.py` for injection modes 1 through 7.

## injector.py

`injector.py` parses both input files into Python ASTs, inserts the top-level statements from a source module into a benign target module, regenerates Python code with `ast.unparse`, and performs a final parse check on the generated output.

It requires Python 3.9+ because it uses `ast.unparse`.

### Inputs

- `--b`: path to the benign Python file.
- `--m`: path to one source Python file to inject.
- `--m_dir`: directory containing multiple source Python files to inject in batch mode.
- `--out`: output file path in single-file mode, or output directory in batch mode.
- `--mode`: injection mode, from `1` to `7`.
- `--seed`: optional random seed for reproducible choices.

`--m` and `--m_dir` are mutually exclusive. Use `--m` for one injected output file, and `--m_dir` for batch generation.

### Injection Modes

- Mode `1`: insert source statements at the head of the benign module.
- Mode `2`: insert source statements in the middle of the benign module.
- Mode `3`: insert source statements at the tail of the benign module.
- Mode `4`: insert source statements at the start of a randomly selected top-level function. Falls back to mode `3` if no function exists.
- Mode `5`: insert source statements at the start of a randomly selected class method. Falls back to mode `4` if no class method exists.
- Mode `6`: split source statements across random global-level insertion slots while preserving source statement order.
- Mode `7`: split source statements across random insertion slots inside a randomly selected function. Falls back to mode `6` if no function exists.

The source module's module-level docstring is removed before injection.

### Single-File Usage

Run from the repository root:

```bash
python inject/injector.py \
  --b malicious_packages_benchmark/benign_injected/bf.py \
  --m malicious_packages_benchmark/malicious_splitable_pyfiles_50/example.py \
  --out malicious_packages_benchmark/malicious_inject_2_benign/example_mode1.py \
  --mode 1 \
  --seed 2025
```

### Batch Usage

```bash
python inject/injector.py \
  --b malicious_packages_benchmark/benign_injected/bf.py \
  --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
  --out malicious_packages_benchmark/malicious_inject_2_benign/1 \
  --mode 1 \
  --seed 2025
```

In batch mode, output files are named with the pattern:

```text
<benign_basename>__with__<source_basename>__mode<mode>.py
```

## run_injector.sh

`run_injector.sh` is a convenience script for running the batch injector across all seven modes.

It uses:

- Benign input file: `malicious_packages_benchmark/benign_injected/bf.py`
- Source directory: `malicious_packages_benchmark/malicious_splitable_pyfiles_50`
- Output root: `malicious_packages_benchmark/malicious_inject_2_benign`
- Random seed: `2025`

Each mode writes to a separate output subdirectory:

```text
malicious_packages_benchmark/malicious_inject_2_benign/1
malicious_packages_benchmark/malicious_inject_2_benign/2
malicious_packages_benchmark/malicious_inject_2_benign/3
malicious_packages_benchmark/malicious_inject_2_benign/4
malicious_packages_benchmark/malicious_inject_2_benign/5
malicious_packages_benchmark/malicious_inject_2_benign/6
malicious_packages_benchmark/malicious_inject_2_benign/7
```

The script uses relative paths. It calls `python injector.py`, so run it from a working directory where `injector.py` is directly available and the `malicious_packages_benchmark/...` paths resolve correctly. If you run from the repository root, update the script to call `python inject/injector.py`; if you run from the `inject` directory, update the dataset paths to point back to the repository root.

Example after adjusting the paths for your working directory:

```bash
bash run_injector.sh
```

You can also run each command manually if you want to modify the input paths, output paths, mode, or seed.
