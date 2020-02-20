from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = 'Njc5OTkzNDEzMTUxNzUyMjQz.Xk52mw.8JLN1ySUDiPyS0c7ulaAvHETA6o'


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

bot.run(token)
