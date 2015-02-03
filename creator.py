from os.path import expanduser
from datetime import datetime, timedelta
from time import strptime, mktime
from icalendar import Calendar, Event

import os
import random
import json
import re


def main():
	# create a calendar
	calendar_name = 'Bilkent Academic Calendar'
	cal = Calendar()
	cal['summary'] = calendar_name
	cal['dtstart'] = '20050404T080000'
	cal.add('prodid', '-//' + calendar_name + '//tuzun.co//')
	cal.add('version', '0.1')

	# get events
	file = open('events.json','r')
	events = json.load(file)
	file.close()

	# split events with multiple days in the same month
	for e in events:
		if (e['date'].find(',') != -1):
			events.remove(e)
			date = e['date'].replace(',', ' ')
			days = re.findall('\d{1,2}[ ]', date)
			tail = re.search('\w+ \d{4}', date).group(0)
			for day in days:
				date = day + tail
				partial_event = {'date': date, 'summary': e['summary'], 'idmyo': e['idmyo']}
				events.append(partial_event)
			
	# add events to the calendar
	for e in events:
		add_event(e, cal)

	# save the calendar
	f = open(os.path.join(expanduser('~'), calendar_name + '.ics'), 'wb')
	print(calendar_name + '.ics has been created in ' + os.path.join(expanduser('~')))
	f.write(cal.to_ical())
	f.close()


def add_event(e, cal):
	event = Event()
	event['uid'] = str(random.randrange(0, 100000000000000000000)) + '@tuzun.co'
	event.add('summary', e['summary'])
	date = e['date']
	if ((date.find('(') == -1) and (date.find('-') == -1)):
		# plain dates
		event.add('dtstart', datetime.fromtimestamp(mktime(strptime(date, '%d %B %Y'))))
	if (date.find('(') != -1):
		# dates with specific time
		event.add('dtstart', datetime.fromtimestamp(mktime(strptime(date, '%d %B %Y (%H:%M)'))))
	if (date.find('-') != -1):
		# dates with range
		dtstart, dtend = date.split(' - ')
		event.add('dtstart', datetime.fromtimestamp(mktime(strptime(dtstart, '%d %B %Y'))))
		event.add('dtend', datetime.fromtimestamp(mktime(strptime(dtend, '%d %B %Y'))) + timedelta(hours=23, minutes=59))
	cal.add_component(event)


if __name__ == "__main__":
    main()
