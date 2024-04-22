import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$mention'):
        await message.channel.send('@everyone tem novidade neste discord!!!')

    if message.content.startswith('$members'):
        for guild in client.guilds:
            for member in guild.members:
                await message.channel.send(member)

client.run('MY_TOKEN')