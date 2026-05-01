import pytest
import tsdlr


def test_sum_as_string():
    assert tsdlr.sum_as_string(1, 1) == "2"
