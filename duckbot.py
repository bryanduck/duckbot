
# duckbot.py

import os
import random


import discord
from dotenv import load_dotenv

from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents(messages=True, guilds=True, message_content=True, presences=True, members=True)

client = discord.Client(intents=intents)

images = list()

for img in os.listdir('C:\\Users\\Bryan\\Desktop\\python bot projects\\duck bot\\duckphotos'): 
    images.append(img)


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if 'duck' in message.content.lower():
		await message.channel.send(file=discord.File('C:\\Users\\Bryan\\Desktop\\python bot projects\\duck bot\\duckphotos\\' + random.choice(images)))
		
#@client.event
#async def on_member_join(member):
#	await member.create_dm()
#	await member.dm_channel.send(
#		f'Hi {member.name}, welcome to my Discord server!'
#	)


client.run(TOKEN)

