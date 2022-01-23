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


                elif msg == '.help':  # done
                    try:
                        file_num = 0

                        while file_num < len(os.listdir('Data\\GitHelpFiles')):
                            with open(f'Data\\GitHelpFiles\\git_help_cmds{file_num}.txt', 'r') as file:
                                file_data = file.read()
                            try:
                                await channel.send(f'{file_data}')

                            except Exception as E:
                                mbed = error_Embed(mesg, E)
                                await error_channel.send(embed=mbed)

                            file_num += 1

                    except IOError as IOE:
                        mbed = error_Embed(mesg, IOE)
                        await error_channel.send(embed=mbed)                   


                elif msg.startswith('.commands'):  # done
                    try:
                        _, query_cmd = msg.split(' ')
                        
                        if len(query_cmd) > 0:
                            cmd_info = getCmdInfo(query_cmd)
                            
                            await channel.send(embed=cmd_info)
                        
                        else:
                            with open('Data\\bot_cmds.txt', 'r') as bot_cmd_file:
                                file_data = bot_cmd_file.read()

                            await channel.send(file_data)
                        
                    except Exception:
                        mbed = lc_Embed('**Missing Argument**', '```One argumennt is required to show the results.\nFor example:-\n\t\t.commands cc```')

                        await channel.send(embed=mbed)
                        

                elif msg.startswith('.cc'):  # done
                    limit = int(msg.replace('.cc ', '')) + 1

                    await channel.purge(limit=limit)


                elif msg == '$reboot$':  # done(admin command)
                    # try:
                    with open(file='Data\\admins.txt', mode='r', encoding='utf-8') as admins_file:
                        _admins = admins_file.readlines()

                    # except IOError as IOE:
                    #     mbed = error_Embed(mesg, IOE)
                    #     await error_channel.send(embed=mbed)

                    formatData(_admins, '\n')

                    member = str(author)

                    if member in _admins:
                        await channel.send(f'**```Command Given By: {member}\nPermission: Granted\nAction: Restarting .Git bot...```**')

                        try:
                            os.system('py .\main_bot.py')

                        except OSError as OSE:

                            mbed = error_Embed(mesg, OSE)
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
