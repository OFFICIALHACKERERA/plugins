from telethon import Button


PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『Lêɠêɳ̃dẞø†』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Lêɠêɳ̃dẞø†』~ `` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/LegendBot_AI)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/LEGEND-AI/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Lêɠêɳ̃dẞø†』 ](https://t.me/LegendBot_OP)\n"
pm_caption += f"┣Assistant ~ By [『Lêɠêɳ̃dẞøy』 ](https://t.me/LegendBoy_XD)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『Lêɠêɳ̃dẞø†』](https://t.me/LegendBot_XD) «««"


@hell_cmd(
    pattern=f"^/alive( )?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    buttons = [
        (Button.url("🔱 Repo 🔱", "https://github.com/LEGEND-AI/LEGENDBOT"),),
    ]
    
