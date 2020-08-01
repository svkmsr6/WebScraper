import requests
import bs4
#import re

def get_entities(class_name):
	res = requests.get('http://quotes.toscrape.com/')
	soup = bs4.BeautifulSoup(res.text,'lxml')
	entities = set([entity.text for entity in soup.select(class_name)])
	return entities

