#!/bin/bash

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/1 \
    --mode 1 \
    --seed 2025

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/2 \
    --mode 2 \
    --seed 2025

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/3 \
    --mode 3 \
    --seed 2025

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/4 \
    --mode 4 \
    --seed 2025

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/5 \
    --mode 5 \
    --seed 2025

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/6 \
    --mode 6 \
    --seed 2025

python injector.py --b malicious_packages_benchmark/benign_injected/bf.py \
    --m_dir malicious_packages_benchmark/malicious_splitable_pyfiles_50 \
    --out malicious_packages_benchmark/malicious_inject_2_benign/7 \
    --mode 7 \
    --seed 2025