import asyncio
from asyncio.tasks import sleep
import discord
from discord.ext import commands
import sys
import random
### for def stock_index { #
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime
# } ###

version = 0.2.5
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
            await channel.send(f"{channel.name}채널이 준비가 되었습니다...")

@client.command(name="목록")
async def order_list(ctx):
    await ctx.send("명령어는 아래와 같아요...")
    await ctx.send("...안녕 : 주인을 맞이하는 인사를 합니다.\n...쉬어 : 주인의 명을 받들어 잠시 대기합니다.\n...차려 : 긴장하며 오와 열을 맞춥니다.\n...팔벌려뛰기 : 명령어 다음 입력받은 횟수까지 팔벌려뛰기를 합니다.\n...업뎃 : 봇을 잠시 중지하고 업데이트 합니다.(구현중)\n...일정 : 구글캘린더에 저장된 오늘의 일정을 메시지로 출력합니다.(구현중)\n...주가 : 현재 코스피 지수를 메시지로 출력합니다.")

@client.command(name="자기소개")
async def hello(ctx):
    await ctx.send(f"저는 mk님의 최초봇 svbot.1 이라고 합니다... \n현재 9개의 명령어 셋을 제공하고 있으며, 이 명령어들은 mk님의 편의와 유희를 위한 기능을 제공하고 있습니다...\n주인님은 ...로 명령어를 시작하며, 저는 대답을 ...로 종결하도록 프로그래밍 되었습니다.\nVersion = {version}...")

@client.command(name="안녕")
async def hello(ctx):
    # print(type(ctx))
    await ctx.send("형님. 잘 지내셨어요...")

@client.command(name="쉬어")
async def relax(ctx):
    await ctx.send("감사합니다. 형님...")

@client.command(name="차려")
async def Charyut(ctx):
    await ctx.send("차렷!...")

@client.command(name="팔벌려뛰기")
async def wide_arm_jump(ctx, count):
    count_int = int(count)
    bIs_dude = random.randint(0,1)
    for i in range(count_int - 1 + bIs_dude):
        await ctx.send(f"{i+1}!")
        await asyncio.sleep(1.0)
    if bIs_dude == 1:
        await ctx.send("정신을 못차렸는지 마지막 구호를 외쳤습니다;; 처음부터 다시!...")
        await asyncio.sleep(1.0)
        await wide_arm_jump(ctx, count)
    # sleep(10.0)

@client.command(name="업뎃")
async def update(ctx):
    await ctx.send("업데이트를 시작합니다. 5초 뒤에 봇이 종료되고 30초 뒤에 재시작합니다...")
    pass

@client.command(name="일정")
async def schedule(ctx):
    await ctx.send("오늘 일정은 아래와 같습니다...")
    pass

@client.command(name="주가")
async def stock_index(ctx):
    basic_url = "https://finance.naver.com/sise/"
    fp = urllib.request.urlopen(basic_url)
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("span",class_="num")
    kospi_value = soup[0].string
    kosdaq_value = soup[1].string
    await ctx.send(f"오늘 KOSPI는 {kospi_value} 입니다...")
    pass

if __name__ == "__main__":
    client.run(sys.argv[1])