import discord
from discord.ext import commands 

client = commands.Bot(command_prefix = '.')
credentials = {}
credentials_name = "credentials.txt"

@client.event
async def on_ready():
    print('Bot is ready.')

def parse_credentials(text_file):
    
    f = open(text_file,'r')

    #get token line
    token = f.readline()
    token = token.split('token:')[1]
    credentials['token'] = token
    
parse_credentials(credentials_name)


client.run(credentials['token'])