from typing import ContextManager
from contextlib import contextmanager
NO_NEWLINE = ''
if False:
    _var_72_0 = (175, 40, 207)
    _var_72_1 = (31, 158, 723)

    def _var_72_fn():
        pass
BELL_CHAR = '\x07'
if False:
    _var_73_0 = (307, 68, 202)
    _var_73_1 = (346, 129, 869)

    def _var_73_fn():
        pass

def bell():
    print(BELL_CHAR, end=NO_NEWLINE)

@contextmanager
def bell_after(play_bell: bool=True) -> ContextManager:
    try:
        yield
    finally:
        if play_bell:
            bell()