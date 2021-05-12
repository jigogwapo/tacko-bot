import os, discord
import discord.ext.commands as commands
from mongoengine import connect
from helpers.custom_text_helpers import get_commands
intents = discord.Intents.all()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
mongodb_uri = os.getenv('MONGODB_URI')

connect('starden', host=mongodb_uri)
print('Connected to database.')

bot = commands.Bot(command_prefix='*', intents=intents)

bot.load_extension('cogs.memes')
bot.load_extension('cogs.books')
bot.load_extension('cogs.info')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.quotes')
bot.load_extension('cogs.todo')
bot.load_extension('cogs.anime')
bot.load_extension('cogs.customtext')

custom_command_list = get_commands()
for command in custom_command_list:
    print(f'Command: {command.command_text}')
    print(f'Text: {command.custom_text}')

    @bot.command(name=command.command_text)
    async def foo(ctx):
        await ctx.send(command.custom_text)

bot.run(TOKEN)