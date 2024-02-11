from bs4 import BeautifulSoup
import requests
import csv

firstname='akshay'
lastname='manoj'
url=f'https://www.linkedin.com/pub/dir?firstName={firstname}&lastName={lastname}&trk=people-guest_people-search-bar_search-submit'

page=requests.get(url)
print(page)
soup=BeautifulSoup(page.text,"lxml")
section =soup.find('section',class_="serp-page__results-list")
boxes=section.find_all('li',class_="pserp-layout__profile-result-list-item")
count=0
for box in boxes:
    count+=1
    if count>5:
        break
    else:
        name=box.find('h3',class_="base-search-card__title").text
        proffession=box.find('h4',class_="base-search-card__subtitle").text
        location=box.find('p',class_='people-search-card__location').text
        uni=box.find('span',class_='entity-list-meta__entities-list').text
    