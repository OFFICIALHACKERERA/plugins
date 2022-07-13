import os

from telethon import Button, events



LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/4f730af88f1d7ec343386.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

LegendBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ ๏ωиэя  ⚜", "https://t.me/OFFICIALHACKERERA")]]
    await tgbot.send_file(event.chat_id, LEGEND_IMG, caption=LegendBoy, buttons=GOOD)
