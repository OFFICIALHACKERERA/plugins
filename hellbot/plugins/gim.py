


@borg.on(admin_cmd(pattern=r"gim", outgoing=True))
async def hapy(event):

    a = "š±āāāāāāš±\nš        \         /          š\nā­          \š/            ā­\nāØ           š½             āØ\n              /    \ \n            š    š"
    await event.edit(a)



CmdHelp("gim").add_command("gim", None, "Get info about a File Extension").add()
