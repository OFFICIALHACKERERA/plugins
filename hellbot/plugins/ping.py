import asyncio
import datetime

from . import *



LEGEND_IMG = "https://te.legra.ph/file/bd44461832cc3ee094547.jpg"



@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**(❛ ᑭσɳց ❜!**")
    if LEGEND_IMG:
        legend_caption = (
            f"**❤️‍🔥 PONG ❤️‍🔥**UP TIME {ms}"
        )
        await event.client.send_file(event.chat_id, LEGEND_IMG, caption=legend_caption)
        await event.delete()


CmdHelp("ping").add_command(
    "ping", None, "Shows you the ping speed of server"
).add_command(
    "hbping", None, "Shows you the ping speed of server with an animation"
    "Official"
).add()

