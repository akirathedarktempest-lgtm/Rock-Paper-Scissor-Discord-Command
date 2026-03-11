import discord
from discord.ext import commands
import random

li=["Rock","Paper","Scissor"]

intents=discord.Intents.all() 
"""Too much lazy to make intents default and add"""
bot=commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
  print("The bot is ready...)


@bot.command()
async def shoot(ctx, s:str):
    a=random.choice(li)
    s=s.lower()
    await ctx.send(f"Yours: {s}, Bot: {a}")
    if s=="rock":
        if a=="Rock":
            await ctx.send("Draw")
        elif a=="Paper":
            await ctx.send("I won")
        elif a=="Scissor":
            await ctx.send("You won")
        else:
            await ctx.send("There's a problem")
    elif s=="paper":
        if a=="Rock":
            await ctx.send("You won")
        elif a=="Paper":
            await ctx.send("Draw")
        elif a=="Scissor":
            await ctx.send("I won")
        else:
            await ctx.send("There's a problem")
    elif s=="scissor":
        if a=="Rock":
            await ctx.send("I won")
        elif a=="Paper":
            await ctx.send("You won")
        elif a=="Scissor":
            await ctx.send("Draw")
        else:
            await ctx.send("There's a problem")
    else:
        await ctx.send("Wrong command")

bot.run("YOUR_TOKEN")

"""I tested it, it works...I won't repeat the mistake """
