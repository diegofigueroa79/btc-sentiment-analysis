import csv
import requests
import xml.etree.ElementTree as ET



def loadRSS():
	
	#url of rss feed
	url = 'https://news.google.com/rss/search?q=bitcoin&hl=en-US&gl=US&ceid=US:en'
	
	#creating HTTP response object from given url
	response = requests.get(url)
	
	# creates xml file
	with open('topnewsfeed.xml', 'wb') as f:
		f.write(response.content)
	
def parseXML(xmlfile):
	
	#create element tree object
	tree = ET.parse(xmlfile)
	
	#get root element
	root = tree.getroot()
	
	#create empty list for news items
	newsitems = []
	
	#iterate news items
	for item in root.findall('./channel/item'):
		
		#iterate child elements of item
		for child in item:
			if (child.tag == 'link'):
				newsitems.append(child.text)
	
	# returns list of news links
	return newsitems
	
def dateXML(xmlfile):
	tree = ET.parse(xmlfile)
	root = tree.getroot()
	newsdates = []
	for item in root.findall('./channel/item'):
		for child in item:
			if (child.tag == 'pubDate'):
				newsdates.append(child.text)
	
	return newsdates
