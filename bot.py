import discord
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

client.run('ODExMjkxNzE5MjIyOTUxOTc4.YCwESg.UU6aPrDb-WHF6bMFMLg1BqFD4cI')
