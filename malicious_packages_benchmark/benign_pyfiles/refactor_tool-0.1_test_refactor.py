# tests/test_refactor.py
from refactor_tool import refactor

def test_find_redundant_code():
    redundant_lines = refactor.find_redundant_code('example.py')
    assert redundant_lines == [2, 4]  # 例として、冗長なコード行を指定