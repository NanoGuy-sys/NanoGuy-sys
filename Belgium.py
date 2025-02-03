import os
import discord
from discord.ext import commands

# Get the bot token from the environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Role IDs (Replace with your actual IDs if they're different)
TRIGGER_ROLE_ID = 1334889005468221570
GIVEN_ROLE_ID = 1334876920005005434

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_member_update(before, after):
    if TRIGGER_ROLE_ID in [role.id for role in after.roles] and TRIGGER_ROLE_ID not in [role.id for role in before.roles]:
        given_role = after.guild.get_role(GIVEN_ROLE_ID)
        if given_role:
            try:
                await after.add_roles(given_role, reason="Trigger role received")
                print(f"Gave role {given_role.name} to {after.name}")
            except discord.Forbidden:
                print(f"Error: Bot lacks permissions to give role {given_role.name}")
            except Exception as e:
                print(f"An error occurred: {e}")

    elif TRIGGER_ROLE_ID in [role.id for role in before.roles] and TRIGGER_ROLE_ID not in [role.id for role in after.roles]:
        given_role = after.guild.get_role(GIVEN_ROLE_ID)
        if given_role:
            try:
                await after.remove_roles(given_role, reason="Trigger role removed")
                print(f"Removed role {given_role.name} from {after.name}")
            except discord.Forbidden:
                print(f"Error: Bot lacks permissions to remove role {given_role.name}")
            except Exception as e:
                print(f"An error occurred: {e}")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready and online!")
    await bot.change_presence(activity=discord.Game(name="Property of Royal Belgium"))

# Start the Discord bot
bot.run(BOT_TOKEN)
