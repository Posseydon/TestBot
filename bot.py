import requests
import mytoken
import json

from bs4 import BeautifulSoup
import urllib3

# from pars import find_fav



token = mytoken.token


URL = 'https://api.telegram.org/bot' + token + '/'
# chat_id
# https://api.telegram.org/bot541327592:AAG6BgSNnaxIr4WLx5yI-dajV6hU1ll53DQ/sendmessage?chat_id=326092086&text=hi

def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()

# We was created the function to find users message positions and chat_id
def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']

	message_text = data['result'][-1]['message']['text']
	
	message = {'chat_id': chat_id,
				'text': message_text}
	return message


def send_message(chat_id, text):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)

# to pars new site to find favicon

def find_fav(url):
	# letter = 'favicon'
	# new_link = []
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	for pos in soup.find_all('link'):
		href = pos.get('href')
		if 'favicon.ico' in href:

			return url + href


def main():
	# d = get_updates()
	
		# to write new json file

	# with open('updates.json', 'w') as f:
	# 	json.dump(d, f, indent=2)
	
	answer = get_message()
	chat_id = answer['chat_id']
	text = answer['text']

	f = find_fav(text)

	if 'https://' in text:
		send_message(chat_id, f)


if __name__ == '__main__':
	main()