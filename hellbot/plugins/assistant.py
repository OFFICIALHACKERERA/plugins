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
        
        



@legend.bot_cmd(pattern="^/ban\\s+([\\s\\S]*)", from_users=Config.OWNER_ID)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id, "`I can't find user to ban`", reply_to=reply_to
        )
    if not reason:
        return await event.client.send_message(
            event.chat_id, "`To ban the user provide reason first`", reply_to=reply_to
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**Error:**\n`{e}`")
    if user_id == Config.OWNER_ID:
        return await event.reply("I can't ban you master")
    check = check_is_black_list(user.id)
    if check:
        return await event.client.send_message(
            event.chat_id,
            f"#Already_banned\
            \nUser already exists in my Banned Users list.\
            \n**Reason For Bot BAN:** `{check.reason}`\
            \n**Date:** `{check.date}`.",
        )
    msg = await ban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@legend.bot_cmd(pattern="^/unban(?:\\s|$)([\\s\\S]*)", from_users=Config.OWNER_ID)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id, "`I can't find user to unban`", reply_to=reply_to
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**Error:**\n`{e}`")
    check = check_is_black_list(user.id)
    if not check:
        return await event.client.send_message(
            event.chat_id,
            f"#User_Not_Banned\
            \n👤 {_format.mentionuser(user.first_name , user.id)} doesn't exist in my Banned Users list.",
        )
    msg = await unban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)



