from __future__ import print_function

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from apiclient.discovery import build
from googleapiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import argparse

# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.send'
store = file.Storage('credentials.json')

def get_credentials():
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[tools.argparser])  # tools as t
        flags = parser.parse_args(args=[])

        creds = tools.run_flow(flow, store, flags=flags)
    return creds

def get_service():
    creds = get_credentials()
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service

def send_messages(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

def print_labels():
    # Call the Gmail API
    service = get_service()
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

def CreateMessageHtml(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw' : raw}
    return body

def main():
    # print_labels()
    msgHtml = "Hi<br/>Html Email"
    msgPlain = "Hi\nPlain Email"
    message = CreateMessageHtml('me','arshdeep.mailme@gmail.com','yeah boiiii',msgHtml,msgPlain)
    service = get_service()
    send_messages(service,'me', message)

main()