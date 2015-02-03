from bs4 import BeautifulSoup
import requests
import html
import json
import re

response = requests.get('http://www.bilkent.edu.tr/bilkent/academic/calendar/')
print('status: ' + str(response.status_code))
soup = BeautifulSoup(response.text)
tables = soup.findAll('table', {'class': 'sample'})

events = []
for table in tables:
	for row in table.findAll('tr'):
		aux = row.findAll('td')
		date = re.sub(r', [A-Z][a-z]+day', r'', aux[0].text)
		summary = html.unescape(aux[1].string)
		event = {}
		event['date'] = ' '.join(date.split())
		event['summary'] = ' '.join(summary.split())
		event['idmyo'] = aux[1].find('span', {'class': 'idmyo'}) is not None
		events.append(event)

file = open('events.json', 'w')
file.write(json.dumps(events, indent = 4))
file.close()
