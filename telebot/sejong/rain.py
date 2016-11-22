Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> import xml.etree.ElementTree as ET
>>> import requests
>>> import urllib.request

>>> from urllib.request import urlopen

>>> url = "http://www.kma.go.kr//wid/queryDFSRSS.jsp?zone=1121573000"

>>> data = requests.get(url)

>>> tree = ET.parse(urlopen('http://www.kma.go.kr//wid/queryDFSRSS.jsp?zone=1121573000'))

>>> root = tree.getroot()

>>> def weather():

	x = 0
	n = [] #list

	for data in root.iter("data"):
		if data.findtext("day")<'1' and data.findtext("pop")>='0' and data.findtext("pop")<='10':
			n.append(int(data.findtext("pop")))
			x = 1
		elif data.findtext("day")<'1' and data.findtext("pop")>='11' and data.findtext("pop")<='50':
			n.append(int(data.findtext("pop")))
			x = 2
		elif data.findtext("day")<'1' and data.findtext("pop")>='51' and data.findtext("pop")<='100':
			n.append(int(data.findtext("pop")))
			x = 3	
	if x == 1 :
		print("강수확률 :",max(n),"%")
		print("비 안 온대")
	elif x == 2 :
		print("강수확률 :",max(n),"%")
		print("비올 것 같아")
	elif x == 3 :
		print("강수확률 :",max(n),"%")
		print("우산 챙기렴")
