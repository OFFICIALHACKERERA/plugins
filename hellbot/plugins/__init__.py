import datetime
import time
rom telethon import TelegramClient
from hellbot import *
from hellbot.clients import *
from hellbot.config import Config
from hellbot.helpers import *
from hellbot.utils import *
from hellbot.random_strings import *
from hellbot.version import __hell__
from hellbot.sql.gvar_sql import gvarstat
from telethon import version

D3VIL_USER = bot.me.first_name
d3krish = bot.uid
d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"
hell_logo = "./hellbot/resources/pics/hellbot_logo.jpg"
cjb = "./hellbot/resources/pics/cjb.jpg"
restlo = "./hellbot/resources/pics/rest.jpeg"
shuru = "./hellbot/resources/pics/shuru.jpg"
shhh = "./hellbot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "Its_HellBot"
my_group = Config.MY_GROUP or "HellBot_Chat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/Broken_Heart_72"
hell_channel = f"[†hê Hêllẞø†]({chnl_link})"
grp_link = "https://t.me/HEPPYLIFI"
hell_grp = f"[Hêllẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# hellbot
