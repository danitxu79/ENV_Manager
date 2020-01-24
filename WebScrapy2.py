from bs4 import BeautifulSoup
import requests
import re
from html.parser import HTMLParser

response = requests.get('https://3d-load.net/')
bs = BeautifulSoup(response.text, 'html.parser')
links = bs.find_all('a')
for link in links:
	print(link.get('href'))
