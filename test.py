#-*-coding: utf-8-*-
from __future__ import print_function
import httplib2
import googleapiclient.discovery as discovery
from pytz import timezone
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
# from google_calendar_api import GCalendar
import datetime

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
from datetime import datetime, tzinfo

# input = '둔촌동'

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


# defaultUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
# plusUrl = str(input) + '날씨'
# basic_url = str(defaultUrl) + str(quote_plus(plusUrl))
# fp = urllib.request.urlopen(str(basic_url))
# source = fp.read()
# fp.close()
# soup = BeautifulSoup(source, 'html.parser')
# soup_tmp = soup.findAll("span",class_="todaytemp")
# soup_num = soup.findAll("span",class_="num")
# soup_lv = soup.findAll("span",class_="lv3")
# soup_indic = soup.findAll("span",class_="indicator")
# soup_q1 = soup.findAll("dt")
# print(soup_q1)




CLIENT_SECRET ='astute-purpose-308615-7415464c1358.json'
SCOPE = 'https://www.googleapis.com/auth/calendar'

class GCalendar:
    # KST = datetime.timezone(datetime.timedelta(hours=9))

    def __init__(self, storage_name):
        self.storage_name = storage_name
        self.storage = Storage(storage_name)

    def build_service(self):
        # Fetch credentials from storage
        credentials = self.storage.get()

        # If the credentials doesn's exist in the storage location then run the flow
        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
            http = httplib2.Http()
            credentials = run_flow(flow, self.storage, http=http)

        http = credentials.authorize(httplib2.http())
        self.service = discovery.build('calendar', 'v3', http=http)

def get_calendar(self,calendar_id):
    for calendar in self.get_calendars():
        if calendar.get("id") == calendar_id:
            return calendar

def get_calendar_id(self, summary):
    for calendar in self.get_calendars():
        if calendar.get("summary").strip() == summary:
            return calendar.get("id")

def get_events(self, calendar_id, start, end):
    eventsResult = self.service.events().list()
    calendarId = calendar_id,
    timeMin=start
    timeMax=end,
    timeZone="Asia/Seoul",
    singleEvents=True,
    orderBy='startTime'.execute()
    return eventsResult.get('items', [])

def insert_event(self, calendar_id, event_name, start, end):
    body = {
        'summary': event_name,
        'description': event_name,
        'start': {
            'dateTime': start,
            'timeZone': 'Asia/Seoul',            
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Asia/Seoul',
        },
    }

    return self.service.events().insert(calendarId=calenda_id, body=body).execute()

def delete_event(self, calendar_id, event_id):
    return self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()

calendar = GCalendar("Calendar.storage")
calendar.build_service()
calendar_id = calendar.get_calendar_id(CALENDAR_HOLIDAY)

today = datetime.date.today()
start = datetime.datetime(today .year, today .month, today .day, 0, 0, 0, tzinfo=GCalendar.KST)
end = start + datetime.timedelta(days=1)
events = calendar.get_events(calendar_id, start.isoformat(), end.isoformat())
for event in events:
    print(event["summary"])