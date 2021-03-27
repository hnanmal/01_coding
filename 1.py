# #-*-coding: utf-8-*-
# import asyncio
# from asyncio.tasks import sleep
# import discord
# from discord.ext import commands
# import sys
# import random
# import urllib.request
# from bs4 import BeautifulSoup
# import json
# from urllib import parse
# from urllib.parse import quote_plus
# from collections import OrderedDict
# from datetime import datetime

# defaultUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
# plusUrl = str("미성동") + '날씨'
# basic_url = str(defaultUrl) + str(quote_plus(plusUrl))
# fp = urllib.request.urlopen(str(basic_url))
# source = fp.read()
# fp.close()
# soup = BeautifulSoup(source, 'html.parser')
# soup_tmp = soup.findAll("span",class_="todaytemp")
# soup_num = soup.findAll("span",class_="num")
# soup_uv = soup.findAll("span",class_="indicator")
# soup_rain = soup.findAll("span",class_="rainfall")
# soup_lv2 = soup.findAll("dd",class_="lv2")
# crnt_temp = soup_tmp[0].string
# crnt_sensible = soup_num[2].string
# crnt_rain = soup_rain[0].text
# # crnt_uv = soup_uv[0].text
# crnt_dust = soup_lv2[0].text
# crnt_dustMicro = soup_lv2[1].text


# print(crnt_rain)
# print(crnt_dust)
# print(crnt_dustMicro)


from google_calendar_api import GCalendar
import datetime

# Check Holiday Calendar
calendar = GCalendar("Calendar.storage")
calendar.build_service()
calendar_id = calendar.get_calendar_id(CALENDAR_HOLIDAY)

today = datetime.date.today()
start = datetime.datetime(today .year, today .month, today .day, 0, 0, 0, tzinfo=GCalendar.KST)
end = start + datetime.timedelta(days=1)
events = calendar.get_events(calendar_id, start.isoformat(), end.isoformat())
for event in events:
    print(event["summary"])