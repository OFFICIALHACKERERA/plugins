import os
import datetime
from telethon import events
from telethon import Button, events

PM_IMG = "https://te.legra.ph/file/fa15573431b4d91a002c7.jpg"
pm_caption = f"Assistant is Online \n\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣❤️‍🔥 Telethon : `1.15.0` \n"
pm_caption += f"┣❤️‍🔥 Version  : `2.0` \n"
pm_caption += f"┣❤️‍🔥 Channel  : [ᴄʜᴀɴɴᴇʟ](https://t.me/Broken_Heart_72)\n"
pm_caption += f"┣❤️‍🔥 Support  : [sᴜᴘᴘᴏʀᴛ](https://t.me/HEPPYLIFI)\n"
pm_caption += f"┣❤️‍🔥 Owner    : [ᴏғғɪᴄɪᴀʟ ʜᴀᴄᴋᴇʀ](https://t.me/OFFICIALHACKERERA)\n"
pm_caption += f"╰────────────\n"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)


PING_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/fa15573431b4d91a002c7.jpg"
)
ms = 4


OFFICIALHACKER = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n    {ms}\n    ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『soon』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url(" Owner ", "https://t.me/OFFICIALHACKERERA")]]
    await tgbot.send_file(event.chat_id, PING_IMG, caption=OFFICIALHACKER, buttons=GOOD)


PINGG_PIC = "https://te.legra.ph/file/4f730af88f1d7ec343386.jpg"

@bot.on(admin_cmd(pattern="^/ping", outgoing=True))
@bot.on(sudo_cmd(pattern="^/ping", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(event, "__**(❛ ⚡️ρσɳɠ⚡️ ❜!**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        d3vil_caption = f"⚡️ρσɳɠ🦋**\n\n⚡️{ms}\n⚡**๏ฬภєг [OFFICIAL HACKER](https://t.me/OFFICIALHACKERERA)"
        await event.client.send_file(
            event.chat_id, PINGG_PIC, caption=d3vil_caption
        )
        await event.delete()

CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your 𝔇3𝔳𝔦𝔩𝔅𝔬𝔱"
).add()





