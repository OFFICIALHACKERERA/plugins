"""

Available Commands:

.sux

.fuk

.kiss"""


import asyncio


CmdHelp("fuck").add_command("fuck", None, "Sexy animation").add_command(
    "sux", None, "Sexy animation"
).add_command("kiss", None, "Sexy animation").add()


@borg.on(admin_cmd("fuck"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    # input_str = event.pattern_match.group(1)

    # if input_str == "fuk":

    await event.edit("fuk")

    animation_chars = ["π       βοΈ", "π     βοΈ", "π  βοΈ", "πβοΈπ¦"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd("sux"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    # input_str = event.pattern_match.group(1)

    # if input_str == "sux":

    await event.edit("sux")

    animation_chars = ["π€΅       π°", "π€΅     π°", "π€΅  π°", "π€΅πΌπ°"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


""


import asyncio


@borg.on(admin_cmd("kiss"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    # input_str = event.pattern_match.group(1)

    # if input_str == "kiss":

    await event.edit("kiss")

    animation_chars = ["π€΅       π°", "π€΅     π°", "π€΅  π°", "π€΅ππ°"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])
