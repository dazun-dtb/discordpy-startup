from discord.ext import commands
import discord
import traceback
token = ""
bot = commands.Bot(command_prefix='!')
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
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'neko':
        await message.channel.send('みゃーん')
        
client.run(token)
