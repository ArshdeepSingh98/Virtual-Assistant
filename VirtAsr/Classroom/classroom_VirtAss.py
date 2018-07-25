from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import argparse

# Setup the Classroom API
SCOPES = 'https://www.googleapis.com/auth/classroom.courses'
store = file.Storage('credentials.json')

def get_credentails():
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[tools.argparser])  # tools as t
        flags = parser.parse_args(args=[])

        creds = tools.run_flow(flow, store, flags=flags)
    return creds;

def get_service():
    creds = get_credentails()
    service = build('classroom', 'v1', http=creds.authorize(Http()))
    return service

def print_courses(service):
    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        for course in courses:
            print(course['name'])

def create_course(service):
    print('Create Course\n')
    print('Enter the Name of course : ')
    name = input()
    print('Enter Section of course : ')
    section = input()
    print('Enter the DescriptionHeading : ')
    descH = input()
    print('Enter Description : ')
    desc = input()
    print('Enter Room Number : ')
    room = input()

    course = {
        'name': name,
        'section': section,
        'descriptionHeading': descH,
        'description': desc,
        'room': room,
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print(u'Course created: {0} ({1})'.format(course.get('name'),course.get('id')))


def create_eg_course(service):
    course = {
        'name': '10th Grade Biology',
        'section': 'Period 2',
        'descriptionHeading': 'Welcome to 10th Grade Biology',
        'description': """We'll be learning about about the structure of living
                     creatures from a combination of textbooks, guest
                     lectures, and lab work. Expect to be excited!""",
        'room': '301',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print(u'Course created: {0} ({1})'.format(course.get('name'), course.get('id')))


def main():
    service = get_service()
    print_courses(service)
    create_eg_course(service)
    create_course(service)

main()