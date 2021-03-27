#-*-coding: utf-8-*-
from __future__ import print_function
import httplib2
import googleapiclient.discovery as discovery
from pytz import timezone
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from datetime import datetime, timezone, timedelta


CLIENT_SECRET ='astute-purpose-308615-7415464c1358.json'
SCOPE = 'https://www.googleapis.com/auth/calendar'

class GCalendar:
    KST = timezone(timedelta(hours=9))

    def __init__(self, storage_name):
        self.storage_name = storage_name
        self.storage = Storage(storage_name)

    def build_service(self):
        # Fetch credentials from storage
        credentials = self.storage.get()

        # If the credentials doesn't exist in the storage location then run the flow
        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
            http = httplib2.Http()
            credentials = run_flow(flow, self.storage, http=http)

        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=http)

    def get_calendar(self, calendar_id):
        for calendar in self.get_calendar():
            if calendar.get("id") == calendar_id:
                return calendar

    def get_events(self, calendar_id, start, end):
        eventsResult = self.service.events().list(
            calendarId = calendar_id,
            timeMin=start,
            timeMax=end,
            timeZone="Asia/Seoul",
            singleEvents=True,
            orderBy='startTime').execute()
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
        return self.service.events().insert(calendarId=calendar_id, body=body).execute()

    def delete_event(self, calendar_id, event_id):
        return self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
