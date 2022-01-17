from discord import Embed, Colour
import random as r


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


all_cmds = []


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
