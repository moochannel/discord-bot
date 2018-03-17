import function

async def getMessage(rpc, client, message):
    if message.content.startswith("!command"):
        responce = function.command.command(rpc, client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!die"):
        if message.author.id == "282462612497891328":
            print("bot logout!")
            await client.send_message(message.channel, "bot Logout!")
            await client.logout()
    
    if message.content.startswith("!getBlockCount"):
        responce = function.getblockcount.getBlockCount(rpc)
        res = "block : " + str(responce)
        print(res)
        await client.send_message(message.channel, res)
    
    if message.content.startswith("!getBlockHash "):
        responce = function.getblockhash.getBlockHash(rpc, client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!getBlock "):
        responce = function.getblock.getBlock(rpc, client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!mining"):
        responce = function.generate.mining(rpc, client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!pre_mining"):
        responce = function.generate.pre_mining(rpc, client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!faucet"):
        responce = function.tip.faucet(rpc, client, message)
        await client.send_message(message.channel, embed=responce)

    if message.content.startswith("!balance"):
        responce = function.balance.getbalance(rpc, client, message)
        await client.send_message(message.channel, embed=responce)
