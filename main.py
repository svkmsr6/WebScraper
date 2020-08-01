import requests
import bs4
#import re

results = requests.get('https://en.wikipedia.org/wiki/Liverpool_F.C.')

soup = bs4.BeautifulSoup(results.text,"lxml")

liv_list = soup.select('.thumbimage')

liv_list_elms = [elm['src'] for elm in liv_list]

print(liv_list_elms[0])
