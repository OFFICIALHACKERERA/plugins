import os
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





HELP_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/fa15573431b4d91a002c7.jpg"
)
ms = 4


OFFICIALHACKER = f"""The commands in the bot are:
**Note : **__This commands work only in this bot__ {botusername}
• **Cmd : **/uinfo <reply to user message>
• **Info : **__You have noticed that forwarded stickers/emoji doesn't have forward tag so you can identify the user who sent thoose messages by this cmd.__
• **Note : **__It works for all forwarded messages. even for users who's permission forward message nobody.__
• **Cmd : **/ban <reason> or /ban <username/userid> <reason>
• **Info : **__Reply to a user message with reason so he will be notified as you banned from the bot and his messages will not be forworded to you further.__
• **Note : **__Reason is must. without reason it won't work. __
• **Cmd : **/unban <reason(optional)> or /unban <username/userid>
• **Info : **__Reply to user message or provide username/userid to unban from the bot.__
• **Note : **__To check banned users list use__ `{cmhd}bblist`.
• **Cmd : **/broadcast
• **Info : **__Reply to a message to get broadcasted to every user who started your bot. To get list of users use__ `{cmhd}bot_users`.
• **Note : **__if user stoped/blocked the bot then he will be removed from your database that is he will erased from the bot_starters list.__
"""



@tgbot.on(events.NewMessage(pattern="^/help"))
async def _(event):
    GOOD = [[Button.url(" Owner ", "https://t.me/OFFICIALHACKERERA")]]
    await tgbot.send_file(event.chat_id, HELP_IMG, caption=OFFICIALHACKER, buttons=GOOD)


