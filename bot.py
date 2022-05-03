import json
import os
import discord
import random
from discord.ext import commands

with open("data.json", "r", encoding="utf-8") as jsonTemp:
    jsonData = json.load(jsonTemp)

yuyuyu = commands.Bot(command_prefix=jsonData['prefix'], intents=discord.Intents.all())

@yuyuyu.event
async def on_ready():
    print(">> Bot is Online <<")

@yuyuyu.event
async def on_member_join(member):
    channel = yuyuyu.get_channel(jsonData["welcome_channel"])
    await channel.send(f"{member} 加入了频道，我们鼓掌。")

@yuyuyu.command()
async def ping(ctx):
    await ctx.send(f"{round(yuyuyu.latency*1000)}(ms)")

@yuyuyu.command()
async def yuyuyumeme(ctx):
    img_number = random.randint(0, 11)
    img = discord.File(jsonData["meme.yuyuyu"][img_number])
    await ctx.send(File=img)

yuyuyu.run(os.environ['DPY_TOKEN'])
