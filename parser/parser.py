#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests, fake_useragent
from time import sleep

# pip3 install fake_useragent
# pip3 install bs4
# pip3 install requests
# pip3 instaal 'requests[socks]'
# systemctl start tor.service

#Just a line
Line = "------------------------------------------------------------------------------------------"

#Random User-Agent
ua = fake_useragent.UserAgent()
user = ua.random
header = {'User-Agent':str(user)}

#Connection to the ip-site
ipSite='http://icanhazip.com'
adress = requests.get(ipSite, header = header)

#Check your ip adress
print(line + "\n[*] IP your network:\n"+adress.text + line)
print("[!] Connecting to the Tor network /", end = "")

#Just point
for i in range(5):
	sleep(0.2)
	print('.', end = '', flush = True)

#Proxie tor's
proxie = {
	'http': 'socks5h://127.0.0.1:9050',
	'https': 'socks5h://127.0.0.1:9050'
}

#Connecting to the network tor
try:
	adress = requests.get(ipSite, proxie = proxie, headers = headers)
#Not connected
except:
	connection = False
	print("/\n[x] Stopping connect to the Tor network\n" + line)

#Connected
else:
	connection = True
	print("/\n[+] Connected to the Tor network\n" + line)
	print("[*] IP Tor network:\n" + adress.text + line)

#Parse site
finally:
	url = input("[!] Uniform Resource Locator:\nhttp://")

	if connection == True:
		page = requests.get("http://"+srt(url.split()[0]), proxie = proxie, header = header)
	else:
		page = requests.get("http://"+str(url.split()[0]), header = header)

	soup = BaeutifulSoup(page.text, "html.parser")

	#Default parse - HTML
	if url.split()[0] == url.split()[-1]:
		code = ""
		for tag in soup.findALL('html'):
			code += str(tag)
		with open("index.html","w") as html:
			html.write(code)
	else:
		#Parse tag
		if url.split()[1] == url.split()[-1]:
			for tag in soup.findALL(url.split()[1]):
				print(tag)
		#Parse attribute
	    else:
		    for tag in soup.findALL(url.split()[1]):
		    	print(tag[url.split()[2]])
	print(line)