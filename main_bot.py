"""
Bot ID- .GIt#8078
"""


print('\n\nACTION: Importing required data... STATUS: ', end='')
import os
from time import sleep as wait

import discord
from discord.utils import get

from Data.quantam import *

print('Done')

# ===========================================================================


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
async def on_message(mesg):
    
    msg = mesg.content
    channel = mesg.channel
    author = mesg.author
    
    
    if (msg.startswith('.')) or (msg == '$reboot$'):
        try:
            _cmd = msg.replace('.', '')
        except Exception:
            pass


        if (checkCMD(_cmd) is True) or (msg == '$reboot$'):

            if str(channel.name) in all_channels:
                mbed = bc_Embed('**channel not suppoerted for commands**', f'**Rule** :eight: \n{server_rules[6]}')
                mbed.set_author(name=author, icon_url=author.avatar_url)

                await channel.send(embed=mbed)
                wait(5.0)
                await channel.purge(limit=2)

            else:

                error_channel = bot.get_channel(932192413026512936)

                if (author == bot.user) or (str(author) == 'MEE6#4876'):
                    pass


                elif msg == '.ping':  # done
                    mbed = lc_Embed("**Ping!**", f'**```Current bot ping: {round(bot.latency * 1000)}ms```**')
                    await channel.send(embed=mbed)


                elif msg.startswith('.help'):  # bugs
                    git_cmd = msg.replace(".help")

                    if len(git_cmd) > 0:
                        pass

                    else:
                        try:
                            with open('Data\\GitHelpFiles\\git_help_cmds.txt', 'r') as git_help_file1:
                                file_data1 = git_help_file1.read()

                            with open('Data\\GitHelpFiles\\git_help_cmds2.txt', 'r') as git_help_file2:
                                file_data2 = git_help_file2.read()

                        except IOError as IOE:
                            mbed = error_Embed(msg, IOE)
                            await error_channel.send(embed=mbed)

                        try:
                            await channel.send(f'{file_data1}\n{file_data2}')

                        except Exception as E:
                            mbed = error_Embed(msg, E)
                            await error_channel.send(embed=mbed)


                elif msg.startswith('.commands'):  # done
                    with open('Data\\bot_cmds.txt', 'r') as bot_cmd_file:
                        file_data = bot_cmd_file.read()

                    await channel.send(file_data)


                elif msg.startswith('.cc'):  # done
                    limit = int(msg.replace('.cc ', '')) + 1

                    await channel.purge(limit=limit)


                elif msg == '$reboot$':  # done(admin command)
                    try:
                        with open('Data\\admins.txt', 'r', encoding='utf-8') as admins_file:
                            admins = admins_file.readlines()

                    except IOError as IOE:
                        mbed = error_Embed(msg, IOE)
                        await error_channel.send(embed=mbed)

                    formatData(admins, '\n')

                    member = str(author)

                    if member in admins:
                        await channel.send(f'**```Command Given By: {member}\nPermission: Granted\nAction: Restarting .Git bot...```**')

                        try:
                            os.system('py .\main_bot.py')

                        except OSError as OSE:

                            mbed = error_Embed(msg, OSE)
                            await error_channel.send(embed=mbed)

                    else:
                        await channel.send(f'**```Command Given By: {member}\nPermission: Denied```**')
                        wait(2.0)
                        await channel.purge(limit=2)

        else:
            if (author == bot.user) or (str(author) == 'MEE6#4876'):
                pass

            else:
                await channel.send(f'**```No such command ->{msg}<-. Use .commands command to see the list of availabe commands```**')
                wait(4.0)
                await channel.purge(limit=2)

    else:
        pass


@bot.event
async def on_member_join(member):

    try:
        role_to_add = get(member.guild.roles, name="Members")
        await member.add_roles(role_to_add)

    except Exception as E:
        mbed = error_Embed('assigning role when member joins', E)
        await bot.get_channel(932192413026512936).send(embed=mbed)



# wakeUp()
bot.run(TOKEN)
