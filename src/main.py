import os
import discord
from discord import permissions
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True


bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    intents=intents,
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = "" # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

# Function that return pong when you "!pong" the bot
# Activate the command with : "!pong"
@bot.command()
async def pong(ctx):
    await ctx.send('pong')

# Function that return the name of the user
# Activate the command with : "!name"
@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

# Function that return the list of all status and the number of people for each status
# Activate the command with : "!count"
@bot.command()
async def count(ctx):
    members = ctx.guild.members
    online = 0
    offline = 0
    idle = 0
    dnd = 0
    invisible = 0

    for member in members:
        if member.status == discord.Status.offline:
            offline+=1
        elif member.status == discord.Status.online:
            online+=1
        elif member.status == discord.Status.idle:
            idle+=1
        elif member.status == discord.Status.dnd:
            dnd+=1
        elif member.status == discord.Status.invisible:
            invisible+=1

    await ctx.send('{online} members are online, {offline} members are offline, {idle} members are idle, {dnd} members have do not disturb activated, {invisible} members are invisible'.
    format(online=online, offline=offline, idle=idle, dnd=dnd, invisible=invisible))

# Function that give the 'Admin' role to the target person
# Activate the command with : "!admin <nickname>"
@bot.command()
async def admin(ctx, name):
    members = ctx.guild.members
    exist = False
    admin_role = ""

    # Get the target member
    for member in members:
        if member.name == name:
            user = member
            break

    # Check if the role is already given
    for role in ctx.guild.roles:
        if role.name == "Admin":
            exist = True
            admin_role = role
            break

    # Check if the role already exists
    if exist:
        await user.add_roles(admin_role)
    # Give the role to the target member
    else:
        role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions(8))
        await user.add_roles(role)

# Function that give the 'Ghost' role to the target person
# Activate the command with : "!mute <nickname>"
@bot.command()
async def mute(ctx, name):
    members = ctx.guild.members
    exist = False
    ghost_role = ""

    # Get the target member
    for member in members:
        if member.name == name:
            user = member
    
    # Check if the role is already given
    for role in ctx.guild.roles:
        if role.name == "Ghost":
            exist = True
            ghost_role = role
            break

    # Check if the role already exists & delete other roles 
    if exist:
        await user.add_roles(ghost_role)
        
    # Give the role to the target member & delete other roles 
    else:
        permissions = discord.Permissions()
        permissions.update(administrator=False, send_messages=False, send_tts_messages=False, read_messages=False, read_message_history=False)
        role = await ctx.guild.create_role(name="Ghost", permissions=permissions)
        await user.add_roles(role)

# Function that ban the target membre
# Activate the command with : "!ban <nickname>"
@bot.command()
async def ban(ctx, name):
    members = ctx.guild.members
    exist = False

    # Get the target member
    for member in members:
        if member.name == name:
            user = member
            exist = True
            break
    
    # Ban the member if he exists
    if exist :
        await user.ban()


token = ""
bot.run(token)  # Starts the bot