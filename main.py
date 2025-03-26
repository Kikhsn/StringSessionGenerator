import os
import subprocess

from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 4790953
API_HASH = "5259225d6fb9bc11b0c839deff993879"

while True:
    subprocess.call(['cls' if os.name == 'nt' else 'clear'], shell=True)
    print("String Session Generator\n")
    print("1. Pyrogram")
    print("2. Telethon")
    print("0. Keluar")
    
    try:
        menu = int(input("\n=> Masukkan Menu: ").lower().strip())
    except (TypeError, ValueError):
        continue
    
    subprocess.call(['cls' if os.name == 'nt' else 'clear'], shell=True)
    
    if menu == 0:
        break
    
    elif menu == 1:
        
        with Client("my_session", api_id=API_ID, api_hash=API_HASH) as app:
            session_string = app.export_session_string()
            subprocess.call(['cls' if os.name == 'nt' else 'clear'], shell=True)
            print("String Session Pyrogram:\n")
            print(session_string)
            print()
    
    elif menu == 2:
        
        with TelegramClient(StringSession(), API_ID, API_HASH) as client:
            session_string = client.session.save()
            subprocess.call(['cls' if os.name == 'nt' else 'clear'], shell=True)
            print("String Session Telethon:\n")
            print(session_string)
            print()
    
    else:
        
        continue
    
    break
