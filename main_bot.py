"""
Bot ID- .GIt#8078
"""


print('\n\nACTION: Importing required data... STATUS: ', end='')
import os
from dotenv import load_dotenv
from time import sleep as wait

import discord

from Data.quantam import *

print('Done')

# ===========================================================================

load_dotenv()

TOKEN = os.getenv('TOKEN')


print('ACTION: preparing bot#8078... STATUS: ', end='')

# code for member intents
intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

print('Ready')


@bot.event
async def on_ready():
    print('Bot is online...')


@bot.event
async def on_message(msg):

    if msg.author == bot.user:
        pass


    elif msg.content == '.ping':
        mbed = lc_Embed("**Ping!**", f'**```Current bot ping: {round(bot.latency * 1000)}ms```**')
        await msg.channel.send(embed=mbed)


    elif msg.content.startswith('.cc'):
        limit = int(msg.content.replace('.cc ', ''))
        
        await msg.content.purge(limit=limit)        


    elif msg.content == '$restart$':  # admin command
        with open('Data\\admins.txt', 'r') as admins_file:
            admins = admins_file.readlines()

        formatData(admins, '\n')

        member = str(msg.author)

        if member in admins:
            await msg.channel.send(f'**```Command Given By: {member}\nPermission: Granted\nAction: Restarting .Git bot...```**')

            try:
                os.system('py .\main_bot.py')

            except OSError as OSE:

                mbed = error_Embed(msg, OSE)
                await bot.get_channel(932192413026512936).send(embed=mbed)

        else:
            await msg.channel.send(f'**```Command Given By: {member}\nPermission: Denied```**')
            wait(2.0)
            await msg.channel.purge(limit=2)


# wakeUp()
bot.run(TOKEN)