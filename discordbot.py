import discord
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
a=0

@client.event
async def on_ready(ctx):
    await ctx.send("起きたよー")

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def win(ctx):
    await ctx.send('勝ち数が１増えたよ')
    global a
    a=a+1
    await ctx.send("あなたの勝ち数は"+str(a))

bot.run(token)
