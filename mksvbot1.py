from asyncio.tasks import sleep
import discord
from discord.ext import commands
import sys
import random

#client = discord.Client()
client = commands.Bot(command_prefix='...')

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("mk.svbot.1")
    await client.change_presence(status=discord.Status.online, activity=game)

    for guild in client.guilds:
        for channel in guild.text_channels:
            await channel.send(f"{channel.name}채널이 준비되었습니다...")


@client.command()
async def 안녕(ctx):
    print(type(ctx))
    await ctx.send("형님. 잘 지내셨어요...")

@client.command()
async def 쉬어(ctx):
    await ctx.send("감사합니다. 형님...")

@client.command(name="차렷")
async def Charyut(ctx):
    await ctx.send("차렷!...")

@client.command()
async def 팔벌려뛰기(ctx, count):
    count_int = int(count)
    bIs고문관 = random.randint(0,1)
    for i in range(count_int - 1 + bIs고문관):
        sleep(0.3)
        await ctx.send(f"{i+1}!")
    if bIs고문관 == 1:
        await ctx.send("저는 마지막 구호를 싸지른 병신입니다! 처음부터 다시!...")
        await 팔벌려뛰기(ctx, count)

@client.command()
async def update(ctx):
    await ctx.send("업데이트를 시작합니다. 5초 뒤에 봇이 종료되고 30초 뒤에 재시작합니다.")
    pass

@client.command()
async def 일정(ctx):
    await ctx.send("오늘 일정은 아래와 같습니다.")
    pass

if __name__ == "__main__":
    client.run(sys.argv[1])