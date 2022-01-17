from discord import Embed, Colour


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