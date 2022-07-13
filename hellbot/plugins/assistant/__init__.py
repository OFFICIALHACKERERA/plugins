# LEGENDBOT Assistant
from telethon import Button, custom


from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


LEGEND_USER = bot.me.first_name
Its_LegendBoy = bot.uid

legend_mention = f"[{LEGEND_USER}](tg://user?id={Its_LegendBoy})"
gban_pic = "./userbot/resources/pics/gban.mp4"
main_pic = "./userbot/resources/pics/main.jpg"
core_pic = "./userbot/resources/pics/core.jpg"
chup_pic = "./userbot/resources/pics/chup.mp4"
bsdk_pic = "./userbot/resources/pics/bsdk.jpg"
bsdkwale_pic = "./userbot/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./userbot/resources/pics/chutiya.jpg"
LEGENDversion = "3.0"

perf = "[ †hê Lêɠêɳ̃dẞø† ]"


DEVLIST = ["2082798662"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
