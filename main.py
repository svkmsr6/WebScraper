import requests
import bs4
import re

results = requests.get('https://en.wikipedia.org/wiki/Liverpool_F.C.')

soup = bs4.BeautifulSoup(results.text,"lxml")

liv_toc = soup.select('.toctext')

liv_toc_headers = [elm.getText() for elm in liv_toc]

print(liv_toc_headers)