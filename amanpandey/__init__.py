# Copright Team ExtremePro (C) 2021-2022
import asyncio
import os
import asyncio
os.system("pip install --upgrade telethon")
from telethon import TelegramClient
from telethon.sessions import StringSession
os.system("pip install --upgrade Extre")
from Extre import *
from Extre.utils import admin_cmd as extremepro_cmd, sudo_cmd as amanpandey_cmd, load_module, humanbytes, tgbot, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin
from Extre.config import Config
from Extre.variables import Var
bot = "ExtremeProUserBot"


# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
