from bs4 import BeautifulSoup
from pprint import pprint
import requests


html_text = requests.get(
    'https://www.mustakbil.com/jobs/search?keywords=React&city=Karachi&countryId=162').text
soup = BeautifulSoup(html_text, 'lxml')

rows = []


jobs = soup.find_all('div', class_='mat-card mb10 list-item')

for job in jobs:
    title = job.find('h2', class_='mb5 mt0 tappable').find('a').text
    details = job.find(
        'div', class_='layout-row layout-wrap layout-gap-15px').text

    description = job.find('div', class_='mt10 mb10').text
    location = job.find('div', class_='flex').text
    posted_date = job.find(
        'div', class_='flex-100px-gap-15px text-right text-muted').text

    rows.append({'title': title, 'details': details,
                'desc': description, 'location': location, 'date': posted_date})


pprint(rows)
