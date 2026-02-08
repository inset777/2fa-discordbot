# 2fa-discordbot
A lightweight Discord bot that generates and sends one-time 2FA-style codes to users via direct message using their Discord ID.

# Discord 2FA DM Bot

A lightweight Python Discord bot that generates and sends one-time verification (2FA-style) codes to users via direct message using their Discord ID.

Built for:
- authentication workflows  
- internal tools  
- automation  
- learning Discord bot development  

> This is NOT Discord’s official 2FA system. It is a custom verification delivery tool.

---

# How It Works

1. Launch the script
2. Enter your Discord bot token
3. Enter the target Discord user ID
4. The bot generates a 6-digit code
5. The bot sends the code via DM
6. The bot exits automatically

---

# Requirements

- Python 3.9+
- discord.py
- Internet connection
- Discord bot token
- Bot added to a server shared with the user

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Setup Guide

## 1) Clone the repository

```bash
git clone https://github.com/inset777/2fa-discordbot.git
```

---

## 2) Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3) Create a Discord bot

Open Discord Developer Portal:

```text
https://discord.com/developers/applications
```

Steps:

1. New Application  
2. Bot → Add Bot  
3. Copy Bot Token  
4. Enable:
   - Message Content Intent  
   - Server Members Intent  

---

## 4) Invite the bot to your server

Go to:

```text
OAuth2 → URL Generator
```

Select:

```
Scopes:
☑ bot

Permissions:
☑ Send Messages
☑ Read Messages/View Channels
```

Open generated URL and invite the bot.

---

## 5) Run the bot

```bash
python3 discord_2fa_bot.py
```

You will be prompted for:

```
Enter your Discord bot token:
Enter the Discord user ID to DM:
```

The bot will send a one-time code to that user.

---

# Important Notes

- The user must share a server with the bot  
- The user must have DMs enabled  
- This is not official Discord authentication  
- Use only for legitimate verification systems  

---

# Integrating With Your App / Database

This bot can act as a 2FA delivery system for other platforms.

Example flow:

```
User logs in → Your backend → Generate code → Store in DB → Bot sends DM
```

---

## Example database structure

users table

```
id | username | discord_id | email
```

2fa_codes table

```
id | user_id | code | expires_at
```

---

## Example Python integration

Generate and store a code:

```python
import random
import sqlite3

def generate_code():
    return str(random.randint(100000, 999999))

def store_code(user_id, code):
    conn = sqlite3.connect("auth.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO twofa_codes (user_id, code) VALUES (?, ?)",
        (user_id, code)
    )
    conn.commit()
    conn.close()
```

Then trigger the bot to send the code.

---

# Converting Bot Into a Service (Recommended)

Instead of manual input, modify the script:

```python
async def send_2fa(discord_id, code):
    user = await client.fetch_user(int(discord_id))
    await user.send(f"Your verification code: {code}")
```

Your backend can call this function automatically when a login happens.

---

# Automation Example

Trigger from backend:

```bash
python3 discord_2fa_bot.py
```

Or pass environment variables:

```bash
export DISCORD_TOKEN=your_token_here
python3 discord_2fa_bot.py
```

---

# Security Best Practices

- Expire codes after 60 seconds  
- Hash codes in database  
- Add rate limiting  
- Log attempts  
- Require login before sending codes  

Never use this for:

- spam  
- impersonation  
- phishing  
- fake “Discord security alerts”  

---

# Roadmap

- REST API version  
- Slash commands  
- Multi-user sending  
- Docker deployment  
- Admin dashboard  
- TOTP support  

---

# Disclaimer

This project is for educational and authentication purposes only.

The developer is not responsible for misuse, abuse, or violations of Discord’s Terms of Service.

---

# License

MIT License

Free to use, modify, and distribute.
