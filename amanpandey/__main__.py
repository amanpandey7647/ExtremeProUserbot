# This File Is Part Of https://github.com/TeamExtremePro/ExtremeProUserbot/
# COPYRIGHT TEAM EXTREMEPRO 2021-2022
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from Extre import *
from Extre.utils import admin_cmd as extremepro_cmd, sudo_cmd as amanpandey_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin
from Extre.config import Config
from Extre.variables import Var
from Extre import bot
EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", True)
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Connecting To Scratch Server")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Connected To Scratch Server")
    else:
        bot.start()
import glob
path = 'assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))   

addons = os.environ.get("addons", True)
if addons == "True" or addons is None:
    try:
        os.system("git clone https://github.com/TeamExtremePro/ExtremeProUserbot.git addons/")
    except BaseException:
        pass
    LOGS.info("Installing packages for addons")
    os.system("pip install -r addons/addons.txt")
    path = "addons/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                if str(BOT_MODE) == "True" and plugin_name in BOTINVALID_PLUGINS:
                    LOGS.info(
                        f"ExtremePro - Addons - BOT_MODE_INVALID_PLUGIN - {plugin_name}"
                    )
                else:
                    load_addons(plugin_name.replace(".py", ""))
                    if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                        LOGS.info(f"ExtremePro - Addons - Installed - {plugin_name}")
            except Exception as e:
                LOGS.info(f"ExtremePro - Addons - ERROR - {plugin_name}")
                LOGS.info(str(e))
else:
    os.system("cp plugins/__init__.py addons/")

import glob

path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))



print("USERBOT Deployed And Working Fine For Assistance Join @EXTREMEPROUSERBOTSUPPORT ")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
