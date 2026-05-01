from contextlib import contextmanager
Dv=print
Dq=True
from typing import ContextManager


Dp =("".join([chr(7)]))
Dm =''


def DH():
  Dv(Dp, end=Dm)


@contextmanager
def DR(play_bell: bool = Dq) -> ContextManager:
  try:
    yield

  finally:
    if play_bell:
      DH()
