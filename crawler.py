from bs4 import BeautifulSoup
import requests
import html
import json
import re


def main():
	# get html data from the Bilkent website
	url = 'http://www.bilkent.edu.tr/bilkent/academic/calendar/'
	print('getting data from ' + url)
	response = requests.get(url)
	print('status: ' + str(response.status_code))
	soup = BeautifulSoup(response.text)
	tables = soup.findAll('table', {'class': 'sample'})

	# create serializable events from the html data
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

	# save events
	file = open('events.json', 'w')
	file.write(json.dumps(events, indent = 4))
	file.close()


if __name__ == "__main__":
    main()
