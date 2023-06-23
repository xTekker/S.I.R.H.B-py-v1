import discord
from discord.ext import commands
from embeds import helpembed, faqembed
from commands import register_commands

# Create the bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Register commands
register_commands(bot)

@bot.event
async def on_ready():
    print("SIRHB Ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='/help'))
    await bot.change_presence(status=discord.Status.online)

# Run the bot
bot.run("YOUR_BOT_TOKEN")
