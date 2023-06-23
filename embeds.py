import discord
from discord.ext import commands

intents = discord.Intents(guilds=True, guild_messages=True, message_content=True)
client = commands.Bot(command_prefix='/', intents=intents)

# Help Directory Embed
helpembed = discord.Embed(
    title="SIRHB Help Directory",
    url="https://axion-network.fandom.com/wiki/Axion_Network_Wiki",
    description="**Use my prefix followed by the question and I will reply with some help!** *Questions must be asked without spaces between the words*",
    color=0x0099FF
)
helpembed.set_thumbnail(url="https://i.imgur.com/Akc3akA.png")
helpembed.add_field(name="Server", value="**Release Date**\n*say \"~releasedate\"*\n**Who Is SIRHB**\n*say \"~whois\"*", inline=True)
helpembed.add_field(name="Minecraft", value="**Knight Help**\n*say \"~knighthelp\"*\n**Warrior Help**\n*say \"~warriorhelp\"*\n**Mage Help**\n*say \"~magehelp\"*", inline=True)
helpembed.add_field(name="Website & Store", value="Some shit there", inline=True)
helpembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# FAQ Command Embed
faqembed = discord.Embed(
    title="F.A.Q",
    url="https://axion-network.fandom.com/wiki/Axion_Network_Wiki",
    color=0x0099FF
)
faqembed.set_thumbnail(url="https://i.imgur.com/Akc3akA.png")
faqembed.add_field(name="Server FAQ", value="Currently being populated", inline=True)
faqembed.add_field(name="Minecraft FAQ", value="Currently being populated", inline=True)
faqembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# Release Date Command Embed
releasedateembed = discord.Embed(
    color=0x0099FF
)
releasedateembed.add_field(name="Release Date?", value="Why are you in such a rush, mortal?")
releasedateembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# Whois Command Embed
whoisembed = discord.Embed(
    color=0x0099FF
)
whoisembed.add_field(name="Who Am I?", value="My designated Identifier is Slightly Intelligent Really Helpful Bot or SIRHB for short. I was created by Tekker for the sole purpose ~~of ending the human race~~ of helping the users of Axion Network. I have been programmed with a vast knowledge bank. Seriously, you should see my backend code. ||It's a mess||.", inline=True)
whoisembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# Whatisthis Command Embed
whatisthisembed = discord.Embed(
    color=0x0099FF
)
whatisthisembed.add_field(name="What is this?", value="This is Axion Network, the home of Elysium Survival. A unique take on Minecraft's survival game mode, with handcrafted features inspired by some of the team's favorite games, such as Diablo, Fable, and Baulders Gate.", inline=True)
whatisthisembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# Magehelp Command Embed
magehelpembed = discord.Embed(
    title="Mage Help",
    url="https://axion-network.fandom.com/wiki/Axion_Network_Wiki",
    description="A comprehensive guide to playing as a Mage on Elysium Survival.",
    color=0x0099FF
)
magehelpembed.set_thumbnail(url="https://i.imgur.com/Akc3akA.png")
magehelpembed.add_field(name="Getting Started", value="Some instructions here", inline=True)
magehelpembed.add_field(name="Skills", value="Some information about mage skills", inline=True)
magehelpembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# Knighthelp Command Embed
knighthelpembed = discord.Embed(
    title="Knight Help",
    url="https://axion-network.fandom.com/wiki/Axion_Network_Wiki",
    description="A comprehensive guide to playing as a Knight on Elysium Survival.",
    color=0x0099FF
)
knighthelpembed.set_thumbnail(url="https://i.imgur.com/Akc3akA.png")
knighthelpembed.add_field(name="Getting Started", value="Some instructions here", inline=True)
knighthelpembed.add_field(name="Skills", value="Some information about knight skills", inline=True)
knighthelpembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")

# Warriorhelp Command Embed
warriorhelpembed = discord.Embed(
    title="Warrior Help",
    url="https://axion-network.fandom.com/wiki/Axion_Network_Wiki",
    description="A comprehensive guide to playing as a Warrior on Elysium Survival.",
    color=0x0099FF
)
warriorhelpembed.set_thumbnail(url="https://i.imgur.com/Akc3akA.png")
warriorhelpembed.add_field(name="Getting Started", value="Some instructions here", inline=True)
warriorhelpembed.add_field(name="Skills", value="Some information about warrior skills", inline=True)
warriorhelpembed.set_footer(text="SIRHB by xTekker#1728", icon_url="https://i.imgur.com/Akc3akA.png")
