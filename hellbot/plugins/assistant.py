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



HELP_LOGO = "https://te.legra.ph/file/bd44461832cc3ee094547.jpg"


help_text = (
        f"** ASSISTANT HELP MENU ** \n"
        f"┏━━━━━━━━━━━━━━━━━━━━\n"
        f"┣[ `/start` - **Start mesajını göndərər.**\n"
        f"┣[ `/id` - **Bir qrup və ya istifadəçi ID almaq üçün.**\n"                               
        f"┣[ `/tr` - **Tərcümə edər.**\n"
        f"┣[ `/help` - **Bu mesajı atar.**\n"
        f"┣[ `/purge` - **Qeyd etdiyiniz mesajdan sonraki mesajları təmizləyər.**\n"
        f"┣[ `/del` - **Cavab verdiyiniz mesajı silər.**\n"
        f"┣[ `/ban` - **Bir istifadəçini ban etmək üçün.**\n"
        f"┣[ `/unban` - **Bir istifadəçinin banını açar.**\n"
        f"┣[ `/promote` - **Bir istifadəçini admin etmək üçün.**\n"
        f"┣[ `/demote` - **Bir istifadəçinin adminlik hüququnu almaq üçün.**\n"
        f"┣[ `/pin` - **Cavab verdiyiniz mesajı sabitləyər.**\n"
        f"┣[ `/lyrics` - **Adını yazdığınız musiqinin sözlərini axtarar.**\n"
        f"┗━━━━━━━━━━━━━━━━━━━━\n"
        )
        
        
@tgbot.on(events.NewMessage(pattern="^/help"))
async def help(event):
    await tgbot.send_file(event.chat_id, HELP_LOGO, caption=help_text)
        
        



