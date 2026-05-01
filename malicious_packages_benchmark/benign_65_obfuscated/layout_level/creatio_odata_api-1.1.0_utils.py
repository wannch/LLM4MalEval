"""Utility functions for the Creatio OData API."""
from rich import print
def print_exception(e:Exception,custom_msg:str="")->None:
  if custom_msg:
    custom_text=f"{custom_msg}: "
  else:
    custom_text=""
  print(f"{custom_text}[red]{e.__class__.__name__}:[/] {str(e)}")