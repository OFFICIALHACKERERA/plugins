from telethon import events

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜ LegendBot is Online ⚜ \n\n"
pm_caption += f"Owner ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Telethon ~ `1.15.0` \n"
pm_caption += f"┣『LegendBot』~ `{LEGENDversion}` \n"
pm_caption += f"┣Channel ~ [Channel](https://t.me/LegendBot_AI)\n"
pm_caption += f"┣**Licenece** ~ [Licence](https://github.com/ITS-LEGENDBOT/LEGENDBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [LegendBot』 ](https://t.me/LegendBot_OP)\n"
pm_caption += f"┣Assistant ~  [『LegendBoy』 ](https://t.me/LegendBoy_XD)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『LegendBot』](https://t.me/LegendBot_OP) «««"

from telethon import events


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
