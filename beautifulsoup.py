from bs4 import BeautifulSoup
import requests
import csv

firstname='akshay'
lastname='m'
url=f'https://www.linkedin.com/pub/dir?firstName={firstname}&lastName={lastname}&trk=people-guest_people-search-bar_search-submit'

page=requests.get(url)
# print(page)
# creating an instance for beautifulsoup lxml as parser
soup=BeautifulSoup(page.text,"lxml")
# needed data are in the section and inside in different boxes
section =soup.find('section',class_="serp-page__results-list")
boxes=section.find_all('li',class_="pserp-layout__profile-result-list-item")
scraped_data = []
count=0
for box in boxes:
    count+=1
    if count>5:
        break
    else:
        name=box.find('h3',class_="base-search-card__title").text
        proffession=box.find('h4',class_="base-search-card__subtitle").text
        location=box.find('p',class_='people-search-card__location').text
        university=box.find('span',class_='entity-list-meta__entities-list').text

        data = {
            'Name': name, 
            'Profession': proffession, 
            'Location': location,
            'University' : university

        }
        scraped_data.append(data)


with open('linkedin_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Profession', 'Location','University']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
         writer.writerow(item)
    