import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot gotowy")

@client.command()
async def hej():
    await client.say("Witaj użytkowniku")
    
@client.command()
async def kontakt():
    await client.say("Jeśli chcesz się skontaktować napisz na: wilk85@gmail.com")

@client.command()
async def ts():
    await client.say("Nasz team-speak 54.36.13.189:10794, napisz na maila po hasło")

@client.command()
async def lista():
    await client.say("Wszystkie komendy dostępne: .hej, .kontakt. .ts")
    

client.run("NTEyMjc3NTg5MjMxMDA5ODA0.Ds3MWA.csHgquflxr-OPS5cTuQ9VzyoW_g")
