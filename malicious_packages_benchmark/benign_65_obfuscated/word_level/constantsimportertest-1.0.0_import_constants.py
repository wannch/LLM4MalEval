import sys
Np=str
Nu=sys.path

from pathlib import Path

def NG(repo: Np):

    # Get path to platform enablement repo
    NU = Np(Path.home())
    NV = NU + f"/repos/{repo}"

    # Dynamically reference platform enablement repo in order to point to Constants.py
    Nu.insert(int("".join([chr(48)]))               , NV)
    import Constants

    return Constants