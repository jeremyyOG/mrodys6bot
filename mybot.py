import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

TOKEN = 'NDg0ODEzNzMzMjAyMjMxMzI2.DmnknQ.rfV-MWUd12RMGwPA0jrComgAXWo'

client = commands.Bot(command_prefix = '!!')

#events

@client.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + client.user.name)
    print ("With the ID: " + client.user.id)

@client.event
async def on_message(message):
    print("A user has send a message")
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles)


#Commands

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="JeremyyOG")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def aboutjeremy(ctx):
    embed = discord.Embed(title="Name", description="Jeremy", color=0x00ff00)
    embed.set_footer(text="Made by Jeremy")
    embed.set_author(name="JeremyyOG")
    embed.add_field(name="Age", value="13", inline=True)
    embed.add_field(name="Hobby's", value="football, gaming", inline=True)
    embed.add_field(name="Girlfriend", value="He doesnt have one lol", inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted')



client.run(TOKEN)
