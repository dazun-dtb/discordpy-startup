import discord
import traceback
import os
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    ch_name = "全体報告部屋"
    for channel in client.get_all_channels():
        if channel.name == ch_name:
            await channel.send("起きたよー")

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'neko':
        await message.channel.send('みゃーん')
        
client.run(token)
