import discord
from discord.ext import commands
import json
import os


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

with open("config/config.json") as f:
    config = json.load(f)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print('1')


bot.run(config["token"])