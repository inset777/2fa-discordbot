import discord
import asyncio
import random

# Ask for token and target user
TOKEN = input("Enter your Discord bot token: ").strip()
USER_ID = input("Enter the Discord user ID to DM: ").strip()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

def generate_2fa_code():
    return str(random.randint(100000, 999999))  # 6-digit code

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    try:
        user = await client.fetch_user(int(USER_ID))
        code = generate_2fa_code()

        await user.send(f"Your 2FA verification code is: **{code}**")
        print("2FA code sent successfully!")

    except Exception as e:
        print("Error sending DM:", e)

    await client.close()

client.run(TOKEN)
