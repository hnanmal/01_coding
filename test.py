#-*-coding: utf-8-*-
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
from datetime import datetime

input = '둔촌동'

# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

# defaultUrl = 'https://www.google.com/search?q='
# plusUrl = quote_plus(str(input)) + '+' + quote_plus('날씨')
# basic_url = str(defaultUrl) + plusUrl
# headers={'User-Agent':user_agent,}
# request = urllib.request.Request(basic_url,None,headers)
# fp = urllib.request.urlopen(request)
# source = fp.read()
# fp.close()
# soup = BeautifulSoup(source, 'html.parser')
# soup_tmp = soup.findAll("span", id= 'wob_pp')
# print(soup_tmp)


defaultUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
plusUrl = str(input) + '날씨'
basic_url = str(defaultUrl) + str(quote_plus(plusUrl))
fp = urllib.request.urlopen(str(basic_url))
source = fp.read()
fp.close()
soup = BeautifulSoup(source, 'html.parser')
soup_tmp = soup.findAll("span",class_="todaytemp")
soup_num = soup.findAll("span",class_="num")
soup_lv = soup.findAll("span",class_="lv3")
soup_indic = soup.findAll("span",class_="indicator")
print(soup_indic[0].text)