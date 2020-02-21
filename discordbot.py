from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
a=0
    
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready():
    await message.channel.send('起きたよー')

@bot.command()
async def win(ctx):
    await ctx.send('勝ち数が１増えたよ')
    global a
    a=a+1
    await ctx.send("あなたの勝ち数は"+str(a))

bot.run(token)
