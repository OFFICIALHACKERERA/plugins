import asyncio
import os
import datetime
from telethon import events
from telethon import Button, events
from telethon.utils import pack_bot_file_id

PM_IMG = "https://te.legra.ph/file/bd44461832cc3ee094547.jpg"
pm_caption = f"Assistant is Online \n\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣❤️‍🔥 Telethon : `1.15.0` \n"
pm_caption += f"┣❤️‍🔥 Version  : `1.3` \n"
pm_caption += f"┣❤️‍🔥 Channel  : [ᴄʜᴀɴɴᴇʟ](https://t.me/Broken_Heart_72)\n"
pm_caption += f"┣❤️‍🔥 Support  : [sᴜᴘᴘᴏʀᴛ](https://t.me/HEPPYLIFI)\n"
pm_caption += f"┣❤️‍🔥 Owner    : [ᴏғғɪᴄɪᴀʟ ʜᴀᴄᴋᴇʀ](https://t.me/OFFICIALHACKERERA)\n"
pm_caption += f"╰────────────\n"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)



PING_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/bd44461832cc3ee094547.jpg"
)
ms = 4


OFFICIALHACKER = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n    {ms}\n    ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『soon』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url(" Owner ", "https://t.me/OFFICIALHACKERERA")]]
    await tgbot.send_file(event.chat_id, PING_IMG, caption=OFFICIALHACKER, buttons=GOOD)





HELP_LOGO = "https://te.legra.ph/file/bd44461832cc3ee094547.jpg"



HELP_caption = f"Assistant Help Menu\n\n"
HELP_caption += f"**╭───────────**\n"
HELP_caption += f"┣🔥 /alive\n"
HELP_caption += f"┣❤️‍🔥 /help \n"
HELP_caption += f"┣🔥 /id \n"
HELP_caption += f"┣❤️‍🔥 /ping \n"
HELP_caption += f"╰────────────\n"

        
        
@tgbot.on(events.NewMessage(pattern="^/help"))
async def help(event):
    await tgbot.send_file(event.chat_id, HELP_LOGO, caption=HELP_caption)
        
        

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




