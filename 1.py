
import asyncio
from asyncio.tasks import sleep
import discord
from discord.ext import commands
import sys
import random
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from urllib.parse import quote_plus
from collections import OrderedDict

input = "미성동"
defaultUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
plusUrl = str(input) + '날씨'
basic_url = str(defaultUrl) + str(quote_plus(plusUrl))
fp = urllib.request.urlopen(str(basic_url))
source = fp.read()
fp.close()
soup = BeautifulSoup(source, 'html.parser')
soup_tmp = soup.findAll("span",class_="todaytemp")
soup_num = soup.findAll("span",class_="num")
if len(soup.findAll("span",class_="rainfall")) == 0 :
    crnt_rain = "None"
else:
    soup_rain = soup.findAll("span",class_="rainfall")
    crnt_rain = soup_rain[0].text

if len(soup.findAll("span",class_="indicator")) == 0 :
    crnt_uv = "None"
else:
    soup_uv = soup.findAll("span",class_="indicator")
    crnt_uv = soup_uv[0].text

soup_detail = soup.findAll("div",class_="detail_box")
crnt_temp = soup_tmp[0].string
crnt_sensible = soup_num[2].string
crnt_detail = soup_detail[0].text
crnt_detail_str = crnt_detail.split(" ")
detail_1 = crnt_detail_str[2]+ " " + crnt_detail_str[3]
detail_2 = crnt_detail_str[4]+ " " + crnt_detail_str[5]
detail_3 = crnt_detail_str[6]+ " " + crnt_detail_str[7]

print(crnt_uv)