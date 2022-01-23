from discord import Embed, Colour

import random as r
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')


def lc_Embed(_title: str, _desc: str):
    mbed = Embed(
        title = _title,
        description = _desc,
        color=Colour.light_grey()
    )

    return mbed


def bc_Embed(_title: str, _desc: str):
    mbed = Embed(
        title = _title,
        description = _desc,
        color=Colour.blue()
    )

    return mbed


def error_Embed(_cmd: str, _error: str):
    mbed = Embed(
        title = f'**Error in: `{_cmd.content}`**',
        description=f"**```{_error}```**\n\n[VISIT]({_cmd.jump_url})",
        color=Colour.random()
    )

    return mbed



all_cmds = ['ping', 'cc',
            'help', 'commands']


all_channels = ['🎫-general', '🔡-meeting-plans', '🎈-off-topic',
                '🧬-commits', '📂-bot-contribution']


server_rules = ["Follow:-\n-Server Rules: #🧾-rules \n-Server Roles: #🧮-roles \n-Server's code of conduct: 📠-code-of-conduct",
                'Verify yourself using `.verify` command in #✌🏼-verify-yourself',
                'Respect staff members and listen to their instruction',
                'Do not provide or request help on projects that may break laws, breach terms of services, or are malicious or inappropriate.',
                'Do not post unapproved advertising.',
                "Keep discussions relevant to the channel topic. Each channel's description tells you the topic.",
                "Use all commands in command supported channels only. Don't spam other channels with bot commands.",
                'Do not help with ongoing exams. When helping with homework, help people learn how to do the assignment without doing it for them.',
                'Change your server profile according to your college detail.',
                'Teachers are requested to remove/ban a student using bot command.'
                ]



# backend functions
def formatData(data: list, dirt: str, replace_with=None):    # done

    if replace_with is None:
        for index, value in enumerate(data):
            if dirt in value:
                data[index] = value.replace(dirt, '')

            else:
                pass

    else:
        for index, value in enumerate(data):
            if dirt in value:
                data[index] = value.replace(dirt, replace_with)

            else:
                pass


def createID(id_len: int, dtype: str):    # done

    _id = dtype

    for i in range(id_len):
        _id += str(r.randint(a=0, b=9))

    return _id


def checkCMD(command):    # done

    validity = False

    for cmd in all_cmds:
        if command.startswith(cmd):
            validity = True
            break

        else:
            pass

    return validity


def getCmdInfo(query):
    help_dict = {}
    
    if query in help_dict:
        mbed = bc_Embed(f'**Query: ``{query}``**', f'**```{help_dict[query]}```**')
        return mbed
    
    else:
        mbed = lc_Embed(f'**Query: ``{query}``**', '**```No such command```**')
        return mbed