from os.path import expanduser
from datetime import datetime, timedelta
from time import strptime, mktime
from icalendar import Calendar, Event

import os
import random
import json
import re

calendar_name = 'Bilkent Academic Calendar'
cal = Calendar()
cal['summary'] = calendar_name
cal['dtstart'] = '20050404T080000'
cal.add('prodid', '-//Bilkent Academic Calendar//tuzun.co//')
cal.add('version', '0.1')

file = open('events.json','r')
events = json.load(file)
file.close()

events_with_multiple_dates = filter(lambda x: (x['date'].find(',') != -1), events)
for e in events_with_multiple_dates:
	dates = e['date'].replace(',', ' ')
	days = re.findall('\d{1,2}[ ]', dates)
	tail = re.search('\w+ \d{4}', dates).group(0)
	for day in days:
		date = day + tail
		partial_event = {'date': date, 'summary': e['summary'], 'idmyo': e['idmyo']}
		events.append(partial_event)

events_plain = filter(lambda x: (not any((c in set('-(,')) for c in x['date'])), events)
events_with_time = filter(lambda x: (x['date'].find('(') != -1), events)
events_with_range = filter(lambda x: (x['date'].find('-') != -1), events)

for e in events_plain:
	event = Event()
	event['uid'] = str(random.randrange(0, 100000000000000000000)) + '@tuzun.co'
	event.add('summary', e['summary'])
	event.add('dtstart', datetime.fromtimestamp(mktime(strptime(e['date'], '%d %B %Y'))))
	cal.add_component(event)

for e in events_with_time:
	event = Event()
	event['uid'] = str(random.randrange(0, 100000000000000000000)) + '@tuzun.co'
	event.add('summary', e['summary'])
	event.add('dtstart', datetime.fromtimestamp(mktime(strptime(e['date'], '%d %B %Y (%H:%M)'))))
	cal.add_component(event)

for e in events_with_range:
	event = Event()
	event['uid'] = str(random.randrange(0, 100000000000000000000)) + '@tuzun.co'
	event.add('summary', e['summary'])
	dates = e['date'].split(' - ')
	dtstart = dates[0]
	dtend = dates[1]
	event.add('dtstart', datetime.fromtimestamp(mktime(strptime(dtstart, '%d %B %Y'))))
	event.add('dtend', datetime.fromtimestamp(mktime(strptime(dtend, '%d %B %Y'))) + timedelta(hours=23, minutes=59))
	cal.add_component(event)

f = open(os.path.join(expanduser('~'), calendar_name + '.ics'), 'wb')
print(calendar_name + '.ics has been created in ' + os.path.join(expanduser('~')))
f.write(cal.to_ical())
f.close()