import discord
from discord.ext import commands
import pyperclip
import desmos_interface
from selenium import webdriver
import pyautogui
import time
from desmos_interface import screenshot


TOKEN = 'NTAxMjQ1OTkxNTM0NzIzMDcy.Dqk5NA.fykIbBCWjl60hqCRszKhOHVlUkA'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Dalton is online')

@client.event
async def on_message(message):
    channel = message.channel

    if message.content.startswith('#help'):
        await client.send_message(channel, 'I am Dalton, the Graphing Calculator' \
                                  ' assistant. You can summon me by typing "#graph".' \
                                  '\nEx: #graph (x^3-x)/(2x)')

    if message.content.startswith('#graph ') and not message.author.bot:
        equation = message.content[7:]
        await client.send_message(channel, f'Graph of {equation}')
        pyperclip.copy(equation)
        await client.send_message(channel, f'Loading graph...')
        screenshot()
        await client.send_file(channel, 'graph.png')
        
client.run(TOKEN)

#TODO: Add constants and type each character
