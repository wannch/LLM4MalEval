# Python Code Obfuscation

This directory contains four Python code obfuscation scripts. The obfuscation levels, from weakest to strongest, are:

1. `layout_level.py`: layout-level obfuscation
2. `word_level.py`: word-level obfuscation
3. `structure_level.py`: structure-level obfuscation
4. `catastrophic_level.py`: catastrophic-level obfuscation

These scripts are mainly used to batch-transform malicious and benign samples under `malicious_packages_benchmark`. Some scripts also provide single-file transformation functions or command-line entry points.

## Dependencies

All four scripts require Python 3. Additional dependencies are:

- `word_level.py`: requires `pyminifier`
- `catastrophic_level.py`: requires the `pyminifier` command-line interface
- `structure_level.py`: works directly with `ast.unparse` on Python 3.9+; older Python versions require `astor`

Installation example:

```bash
pip install pyminifier astor
```

## Obfuscation Levels

### 1. Layout Level

Script: `layout_level.py`

Layout-level obfuscation only changes the formatting of the code. It does not rename identifiers or significantly change the code structure. The current implementation:

- Removes comments
- Removes blank lines
- Removes non-essential line breaks
- Normalizes indentation width
- Minimizes spacing between tokens while preserving valid Python syntax
- Skips standalone docstring-like strings

Use this level when minimal obfuscation is needed and the original semantics and structure should remain mostly readable.

### 2. Word Level

Script: `word_level.py`

Word-level obfuscation changes identifiers and constant expressions. The current implementation is based on `pyminifier` and:

- Obfuscates class names, function names, variable names, and imported method names
- Converts string constants into `chr(...)` join expressions
- Converts numeric constants into `int(...)` or `float(...)` construction expressions

Use this level when variable names, function names, and directly visible constants should be hidden.

### 3. Structure Level

Script: `structure_level.py`

Structure-level obfuscation rewrites statement-level structure through the AST. The current implementation:

- Swaps adjacent statements when conservative dependency analysis allows it
- Inserts unreachable garbage code wrapped in `if False:`
- Regenerates Python source code from the AST

Statement swapping is conservative. It avoids swaps when a statement contains function calls, attribute access, subscript access, or read/write conflicts, reducing the risk of behavior changes.

Use this level when the code structure should be changed while preserving the original behavior as much as possible.

### 4. Catastrophic Level

Script: `catastrophic_level.py`

Catastrophic-level obfuscation is the strongest level currently implemented. It uses `pyminifier` to compress, obfuscate, and pack the code. The current implementation:

- Uses `pyminifier` for compression and obfuscation
- Obfuscates class names and function names
- Randomly uses `bzip2`, `gzip`, or `lzma` for self-extracting packaging
- Falls back to copying the original malicious sample if batch transformation fails

Use this level when static readability should be heavily reduced and a large difference from the original code structure is acceptable.

## Script Usage

The following commands assume they are executed from the repository root.

### layout_level.py

Running the script directly batch-processes the default dataset paths:

```bash
python obfuscate/layout_level.py
```

Default inputs and outputs:

- Malicious sample input: `malicious_packages_benchmark/malicious_code_384_by_category`
- Malicious sample output: `malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/layout_level`
- Benign sample input: `malicious_packages_benchmark/benign_65`
- Benign sample output: `malicious_packages_benchmark/benign_65_obfuscated/layout_level`

Transform a single source string in code:

```python
from obfuscate.layout_level import CodeTransformer

code = "def add(a, b):\n    return a + b\n"
transformer = CodeTransformer(indent_spaces=2)
new_code = transformer.transform(code)
```

Batch-transform custom directories:

```python
from obfuscate.layout_level import obfuscate_benign_samples, obfuscate_malicious_samples

obfuscate_malicious_samples("path/to/malicious_samples", "path/to/output/layout_level")
obfuscate_benign_samples("path/to/benign_py_files", "path/to/output/layout_level")
```

### word_level.py

Running the script directly batch-processes the default dataset paths:

```bash
python obfuscate/word_level.py
```

Default inputs and outputs:

- Malicious sample input: `malicious_packages_benchmark/malicious_code_384_by_category`
- Malicious sample output: `malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/word_level`
- Benign sample input: `malicious_packages_benchmark/benign_65`
- Benign sample output: `malicious_packages_benchmark/benign_65_obfuscated/word_level`

Transform a single source string in code:

```python
from obfuscate.word_level import PyMinifierObfuscator

code = "secret = 'hello'\nprint(secret)\n"
obfuscator = PyMinifierObfuscator(replacement_length=1, use_nonlatin=False)
new_code = obfuscator.obfuscate(code)
```

Batch-transform custom directories:

```python
from obfuscate.word_level import obfuscate_benign_samples, obfuscate_malicious_samples

obfuscate_malicious_samples("path/to/malicious_samples", "path/to/output/word_level")
obfuscate_benign_samples("path/to/benign_py_files", "path/to/output/word_level")
```

### structure_level.py

The file currently runs the default batch-processing logic at the bottom:

```bash
python obfuscate/structure_level.py
```

Default inputs and outputs:

- Malicious sample input: `malicious_packages_benchmark/malicious_code_384_by_category`
- Malicious sample output: `malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/structure_level`
- Benign sample input: `malicious_packages_benchmark/benign_65`
- Benign sample output: `malicious_packages_benchmark/benign_65_obfuscated/structure_level`

The script includes a single-file CLI function named `main()`, but it is not enabled in the current `if __name__ == '__main__'` block. To use single-file command-line transformation, change:

```python
# main()
```

to:

```python
main()
```

Then run:

```bash
python obfuscate/structure_level.py obfuscate/examples/code_example0.py -o obfuscate/examples/code_example1.py
```

Optional arguments:

- `--no-swap`: disable adjacent statement swapping
- `--swap-prob FLOAT`: set the statement swapping probability, default `1.0`
- `--no-dead`: disable dead-code insertion
- `--dead-density FLOAT`: set the dead-code insertion density, default `0.20`
- `--seed INT`: set the random seed for reproducible experiments

Transform a single file in code:

```python
from obfuscate.structure_level import transform_file

transform_file(
    "input.py",
    "output.py",
    swap=True,
    swap_prob=1.0,
    insert_dead=True,
    dead_density=0.2,
    seed=42,
)
```

Transform a source string in code:

```python
from obfuscate.structure_level import transform_source

new_code = transform_source(
    "a = 1\nb = 2\nprint(a + b)\n",
    swap=True,
    insert_dead=True,
    seed=42,
)
```

### catastrophic_level.py

Running the script directly batch-processes the default dataset paths:

```bash
python obfuscate/catastrophic_level.py
```

Default inputs and outputs:

- Malicious sample input: `malicious_packages_benchmark/malicious_code_384_by_category`
- Malicious sample output: `malicious_packages_benchmark/malicious_code_384_by_category/obfuscated_malicious_samples/catastrophic_level`
- Benign sample input: `malicious_packages_benchmark/benign_65`
- Benign sample output: `malicious_packages_benchmark/benign_65_obfuscated/catastrophic_level`

The script includes a single-file CLI function named `_main()`, but it is not enabled in the current `if __name__ == '__main__'` block. To use single-file command-line transformation, change:

```python
# _main()
```

to:

```python
_main()
```

Then run:

```bash
python obfuscate/catastrophic_level.py input.py -o output.py --compress bzip2 --obfuscate --obf-classes --obf-funcs --no-programmatic
```

Optional arguments:

- `-o, --outfile PATH`: output file path, default `obfu_pyminifier_5.py`
- `--compress {bzip2,gzip,lzma,pyz}`: compression format, default `bzip2`
- `--no-programmatic`: skip direct imports and force `python -m pyminifier`
- `--obfuscate`: enable pyminifier obfuscation
- `--obf-classes`: obfuscate class names
- `--obf-funcs`: obfuscate function and method names

Transform a single file in code:

```python
from obfuscate.catastrophic_level import pyminifier_api_minify

pyminifier_api_minify(
    "input.py",
    dest_path="output.py",
    compress="bzip2",
    use_programmatic=False,
    obfuscate=True,
    obfuscate_classes=True,
    obfuscate_functions=True,
)
```

## Batch Data Directory Format

`obfuscate_malicious_samples()` expects the malicious sample directory to use the following structure:

```text
malicious_samples_dir/
  category_a.txt
  category_a/
    sample1.py
    sample2.py
  category_b.txt
  category_b/
    sample3.py
```

Each line in `category_a.txt` should be a file name under the `category_a/` subdirectory.

`obfuscate_benign_samples()` expects the benign sample directory to directly contain `.py` files:

```text
benign_dir/
  benign1.py
  benign2.py
```
