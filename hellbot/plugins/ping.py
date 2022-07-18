import asyncio
import datetime

from . import *

PING_PIC = "https://telegra.ph/file/e15a2fe1430358e26713c.jpg"

@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(event, "__**⚡ Pong! ⚡**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        d3vil_caption = f"⚡️ρσɳɠ🦋**\n\n⚡️{ms}\n⚡**๏ฬภєг [OFFICIAL HACKER](https://t.me/OFFICIALHACKERERA)"
        await event.client.send_file(
            event.chat_id, PING_PIC, caption=d3vil_caption
        )
        await event.delete()

CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your 𝔇3𝔳𝔦𝔩𝔅𝔬𝔱"
).add()


