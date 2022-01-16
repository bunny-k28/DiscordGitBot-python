"""
Bot ID- .GIt#8078
"""


print('\n\nACTION: Importing required data... STATUS: ', end='')
import datetime as dt
import os
from dotenv import load_dotenv

import discord
from discord import Colour as c
from discord.utils import get

from webServer import wakeUp

print('Done')

# ===========================================================================

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = discord.Client()


@bot.event
async def on_ready():
    print('Bot is online...')


@bot.event
async def on_message(msg):
    
    if msg.author == bot.user:    # done
        pass
    
    
    elif msg.content.startswith('.check'):
        await msg.channel.send('**```Perfectly working```**')


wakeUp()

bot.run(TOKEN)