import discord
import traceback
import os
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
channel_debug=699470415969648671

@client.event
async def on_ready():
    CHANNEL_ID = channel_debug
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('起きたよー')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'neko':
        await message.channel.send('みゃーん')
        
client.run(token)
