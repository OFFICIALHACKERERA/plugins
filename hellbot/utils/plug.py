import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, InputMessagesFilterDocument

from hellbot import *
from hellbot.clients import *
from hellbot.helpers import *
from hellbot.config import *
from hellbot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from hellbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins

def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import hellbot.utils

        path = Path(f"hellbot/plugins/{shortname}.py")
        name = "hellbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Lêɠêɳ̃dẞø† ~ " + shortname)
    else:
        import hellbot.utils

        path = Path(f"hellbot/plugins/{shortname}.py")
        name = "hellbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = hellbot
        mod.borg = bot
        # mod.hellbotBOT = hellbot
        mod.hellbotBot = hellbotBot
        mod.tbot = hellbotBot
        mod.hellbot = hellbot
        mod.tgbot = bot.tgbot
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = hellbot.utils
        mod.Config = Config
        mod.edit_or_reply = edit_or_reply
        mod.delete_hellbot = delete_hellbot
        mod.eod = delete_hellbot
        mod.admin_cmd = admin_cmd
        mod.hellbot_cmd = admin_cmd
        mod.sudo_cmd = sudo_cmd
        # support for hellbotBOT originals
        sys.modules["hellbotBOT.utils"] = hellbot.utils
        sys.modules["hellbotBOT"] = hellbot
        # support for paperplaneextended
        sys.modules["hellbot.events"] = hellbot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["hellbot.plugins." + shortname] = mod
        LOGS.info("🔥⚡Lêɠêɳ̃dẞø†⚡🔥 ~ " + shortname)


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"hellbot/plugins/assistant/{shortname}.py")
        name = "hellbot.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Assistant Bot.")
        print("Assistant Sucessfully imported " + shortname)
    else:
        path = Path(f"hellbot/plugins/assistant/{shortname}.py")
        name = "hellbot.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["hellbot.plugins.assistant" + shortname] = mod
        print("[🤴Assistant🤴 3.0] ~ HAS ~ 💞Installed💞 ~" + shortname)



# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"hellbot.plugins{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel:
        LOGS.info(" 💞Installed💞  - PLUGIN CHANNEL DETECTED.")
        LOGS.info(" 💞Installed💞  - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"hellbot/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "hellbot/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# hellbot
