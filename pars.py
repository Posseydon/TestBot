
import requests
from bs4 import BeautifulSoup
import urllib3



def find_fav(url):
	# letter = 'favicon'
	# new_link = []
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	for pos in soup.find_all('link'):
		href = pos.get('href')
		if 'favicon.ico' in href:

			return url + href
	

	# for icon in favicon:
	# 	if letter in favicon:
	# 		new_link.append(icon)
	# 		return new_link
# print (find_fav('https://djbook.ru'))