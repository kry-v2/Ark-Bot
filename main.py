import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if token:
        bot.run(token)
    else:
        print("Fehler: Kein Token gefunden!")