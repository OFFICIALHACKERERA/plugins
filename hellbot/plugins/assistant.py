import os
from telethon import Button, events





#....................................botalive
PM_IMG = "https://te.legra.ph/file/4f730af88f1d7ec343386.jpg"
pm_caption = f"⚜『Assistant』Is Ôñĺîne⚜ \n\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Broken_Heart_72)\n"
pm_caption += f"┣Support ~ [『join』 ](https://t.me/HEPPYLIFI)\n"
pm_caption += f"┣Assistant ~ By [『OFFICIAL HACKER』 ](https://t.me/OFFICIALHACKERERA)\n"
pm_caption += f"╰────────────\n"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
    
    


#...............................botping

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




#...................................id

@tgbot.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                ),
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await tgbot.send_message(
            event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id))
        )



