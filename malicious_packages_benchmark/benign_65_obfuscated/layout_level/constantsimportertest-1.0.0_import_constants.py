import sys
from pathlib import Path
def get_constants(repo:str):
  home=str(Path.home())
  platform_enablement_repo_path=home+f"/repos/{repo}"
  sys.path.insert(0,platform_enablement_repo_path)
  import Constants
  return Constants
