import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, Discord!")

bot.run("YOUR_BOT_TOKEN")