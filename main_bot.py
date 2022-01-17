"""
Bot ID- .GIt#8078
"""


print('\n\nACTION: Importing required data... STATUS: ', end='')
import os
from dotenv import load_dotenv
from time import sleep as wait

import discord
from discord.utils import get

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
    if msg.content.startswith('.'):
        try:
            _cmd = msg.content.replace('.', '')
        except Exception:
            pass
                    
        
        if (checkCMD(_cmd) is True) or (msg.content == '$reboot$'):
            
            if (msg.author == bot.user) or (str(msg.author) == 'MEE6#4876'):
                pass


            elif msg.content == '.ping':  # done
                mbed = lc_Embed("**Ping!**", f'**```Current bot ping: {round(bot.latency * 1000)}ms```**')
                await msg.channel.send(embed=mbed)


            elif msg.content.startswith('.help'):
                with open('Data\\git_help_cmds.txt', 'r') as git_help_file:
                    file_data = git_help_file.read()

                await msg.channel.send(file_data)


            elif msg.content.startswith('.commands'):
                with open('Data\\bot_cmds.txt', 'r') as bot_cmd_file:
                    file_data = bot_cmd_file.read()

                await msg.channel.send(file_data)


            elif msg.content.startswith('.cc'):  # done
                limit = int(msg.content.replace('.cc ', '')) + 1
                
                await msg.channel.purge(limit=limit)        


            elif msg.content == '$reboot$':  # done(admin command)
                try:
                    with open('Data\\admins.txt', 'r', encoding='utf-8') as admins_file:
                        admins = admins_file.readlines()
                        
                except IOError as IOE:
                    mbed = error_Embed(msg, IOE)
                    await bot.get_channel(932192413026512936).send(embed=mbed)

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

        else:
            if (msg.author == bot.user) or (str(msg.author) == 'MEE6#4876'):
                pass
            
            else:
                await msg.channel.send(f'**```No such command ->{msg.content}<-. Use .commands command to see the list of availabe commands```**')
                wait(4.0)
                await msg.channel.purge(limit=1)

    else:
        pass


@bot.event
async def on_member_join(member):
    pass




# wakeUp()
bot.run(TOKEN)