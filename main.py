from elasticsearch import Elasticsearch
from xml_parser import loadRSS, parseXML, dateXML
from article_crawler import get_news
from json_serializer import write_json
from index_mapping import create_index


def main():
	
	#load rss from web to create xml file
	loadRSS()
	
	#parse through xml file and take out each link and date
	newsitems = parseXML('topnewsfeed.xml')
	newsdates = dateXML('topnewsfeed.xml')
	
	# create list of dictionaries for {article object, article date}
	articles = []
	
	for item, date in zip(newsitems, newsdates):
		articles.append(get_news(item, date))
	
	#clean data by removing None values
	articles = list(filter(None, articles))
	
	for article in articles:
		write_json(article)
	
	print("ALL DONE")

if __name__ == "__main__":
	
	es = Elasticsearch()
	
	if (es.indices.exists(index="bitcoin_index")):
		print("bitcoin_index exists")
	else:
		print("bitcoin_index doesn't exist")
		create_index()
	
	main()