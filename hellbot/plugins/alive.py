import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from hellbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>π₯π₯Userbot Ι¨s ΦΥΌΚΙ¨ΥΌΙπ₯π₯</b></i>
<i><b>βΌ ΓwΓ±Γͺr β</i></b> : γ <a href='tg://user?id={}'>{}</a> γ
β­ββββββββββββββ
β£β <b>Β» Telethon ~</b> <i>{}</i>
β£β <b>Β» userbot ~</b> <i>{}</i>
β£β <b>Β» Sudo ~</b> <i>{}</i>
β£β <b>Β» Uptime ~</b> <i>{}</i>
β£β <b>Β» Ping ~</b> <i>{}</i>
β°ββββββββββββββ
<b><i>Β»Β»Β» <a href='https://t.me/OFFICIALHACKERERA'>[ owner ]</a> Β«Β«Β«</i></b>
"""

msg = """{}\n
<b><i>π π±ππ ππππππ π</b></i>
<b>Telethon β</b>  <i>{}</i>
<b>HΓͺllαΊΓΈβ  β</b>  <i>{}</i>
<b>Uptime β</b>  <i>{}</i>
<b>Abuse β</b>  <i>{}</i>
<b>Sudo β</b>  <i>{}</i>
"""
#-------------------------------------------------------------------------------

@hell_cmd(pattern="hkr$")
async def up(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://te.legra.ph/file/4f730af88f1d7ec343386.jpg"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, HELL_USER, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=PIC, caption=omk, parse_mode="HTML")
    await hell.delete()



@hell_cmd(pattern="alive$")
async def hell_a(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>Β»Β» Π½ΡββΠ²ΟΡ ΞΉΡ ΟΠΈβΞΉΠΈΡ Β«Β«</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hkr", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "β Harmless Module"
).add()
