import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

client = Bot(description="Battle-Bot", command_prefix=".", pm_help = False)
TOKEN = "NDYxNTgzMjQ5OTE1NzcyOTI5.DhbfuQ.w4QW0HBQLEeC0VqJwns4FZ0pyGE"

ATTACK = ["Your attack did 10 damage!", "Critical hit! 20 damage taken by the other player!", "Oops, you missed. 0 damage done.", "Your attack was barely dodged by the other player! Your attack did 5 damage.", "Looks like that attack didn't work very well.. Your attack did 5 damage."]
HEAL = ["Good thing you had that random dinasaur bandage in your backpack! Healed 10 heath!", "That did absolute shit. Healed 0 heath.", "Water keeps the body hydrated! Healed 5 health.", "Stop trying to Laura Croft this; you can't. Healed 0 health.", "Apparently applying a doggo to your wounds help? Healed 5 health?", "Stumbled upon the ***ULTRA RARE HEALER!*** Healed 20 health!", "That did absolute shit for you, bud. Healed 0 health.", "Even though Kool-Aid may heal your emotional problems, it definitely doesn't heal your physical wounds. Healed 0 health.", "Healed 10 health!", "Healed 5 health!", "An apple a day keeps the doctor away! Healed 5 health.", "Healed 10 health!", "Healed 5 health!", "Wacking yourself with a stick doesn't heal you, bud. Healed 0 health."]


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	
	return await client.change_presence(game=discord.Game(name="a deathmatch"))


@client.event
async def on_message(message):
        if message.content.upper().startswith(".HELLO"):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> Greetings. Use .START to start a game!" % (userID))
        if message.content.upper().startswith(".START"):
                await client.send_message(message.channel, "Starting game... done! --->")
        if message.content.upper().startswith(".CHARACTER SET"):
                args = message.content.split(" ")
                await client.send_message(message.channel, "Character Selected: %s" % (" ".join(args[2:])))
        if message.content.upper().startswith(".ATTACK"):
                await client.send_message(message.channel, random.choice(ATTACK))
        if message.content.upper().startswith(".DEFEND"):
                await client.send_message(message.channel, "You defended yourself this turn. All damage taken for that turn is halved.")
        if message.content.upper().startswith(".HEAL"):
                await client.send_message(message.channel, random.choice(HEAL))
        if message.content.upper().startswith(".WINNER"):
                args = message.content.split(" ")
                await client.send_message(message.channel, "Congrats to the winner, %s !" % (" ".join(args[1:])))
        if message.content.upper().startswith(".RULES"):
                await client.send_message(message.channel, "Each player starts with 100 health. As the game goes along, you'll need to subtract- or add- a certain amount based on that displayed. You take turns, alternating between you. Use .Attack to launch an attack, .Defend to defend yourself and .Heal to attempt a heal. Bare in mind that although defending will work 100% of the time, healing and attacking will not.") 
        if message.content.upper().startswith(".END"):
                await client.send_message(message.channel, "--------")


client.run(TOKEN)
