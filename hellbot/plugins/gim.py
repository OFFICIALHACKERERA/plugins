


@borg.on(admin_cmd(pattern=r"gim", outgoing=True))
async def hapy(event):

    a = "🎱➖✊➖➖✊➖🎱\n🌟        \         /          🌟\n⭐          \😁/            ⭐\n✨           🎽             ✨\n              /    \ \n            👟    👟"
    await event.edit(a)



CmdHelp("gim").add_command("gim", None, "Get info about a File Extension").add()
