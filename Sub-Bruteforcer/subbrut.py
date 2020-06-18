#!/usr/bin/env python

import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

t_url = "google.com" # change this to your target url

with open("wordlist.txt", 'r') as wordlist:
	for line in wordlist:
		word = line.strip()
		url = word + '.' + t_url
		response = request(url)
		if response:
			print("0_- Discovered subdomain --> " + url)
