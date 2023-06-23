import discord
from discord.ext import commands

intents = discord.Intents(guilds=True, guild_messages=True, message_content=True)
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print("SIRHB Ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='/help'))
    await client.change_presence(status=discord.Status.online)


@client.command()
async def status(ctx):
    await ctx.send("SIRHB Ready - Errors: 0 - Bot Ver: 1.0")


@client.command()
async def ping(ctx):
    await ctx.send("Really? Im an artificially intelligent bot and the best you can do is /ping? Shame.")


@client.command()
async def help(ctx):
    # Define the helpembed here
    await ctx.send(embed=helpembed)


@client.command()
async def faq(ctx):
    # Define the faqembed here
    await ctx.send(embed=faqembed)


@client.command()
async def releasedate(ctx):
    # Define the releasedateembed here
    await ctx.send(embed=releasedateembed)


@client.command()
async def whois(ctx):
    # Define the whoisembed here
    await ctx.send(embed=whoisembed)


@client.command()
async def whatisthis(ctx):
    # Define the whatisthisembed here
    await ctx.send(embed=whatisthisembed)


@client.command()
async def magehelp(ctx):
    # Define the magehelpembed here
    await ctx.send(embed=magehelpembed)


@client.command()
async def knighthelp(ctx):
    # Define the knighthelpembed here
    await ctx.send(embed=knighthelpembed)


@client.command()
async def warriorhelp(ctx):
    # Define the warriorhelpembed here
    await ctx.send(embed=warriorhelpembed)


@client.command()
async def shrob(ctx):
    # Define your shrobembed here
    await ctx.send(embed=shrobembed)


client.run("Token")
