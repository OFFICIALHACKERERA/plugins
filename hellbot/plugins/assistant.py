from telethon import events
from userbot import *
from . import *
from telethon.tl.functions.users import GetFullUserRequest
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import bot
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)



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
    
    



BOT_PING_PIC = "https://te.legra.ph/file/4f730af88f1d7ec343386.jpg"

ms = 4


LegendBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『😶』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ OFFICIAL HACKER ⚜", "https://t.me/OFFICIAL HACKER")]]
    await tgbot.send_file(event.chat_id, BOT_PING_PIC, caption=LegendBoy)




