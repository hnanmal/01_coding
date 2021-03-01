from oauth2client.service_account import ServiceAccountCredentials
scopes = ['https://www.googleapis.com/auth/calendar']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'server_account.json', scopes)


from httplib2 import Http
http_auth = credentials.authorize(Http())


from apiclient.discovery import build
service = build('calendar', 'v3', http=http_auth)
