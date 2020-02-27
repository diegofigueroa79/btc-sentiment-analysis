import json
from elasticsearch import Elasticsearch


	
def save_to_elasticsearch(json_article):
	
	try:
		client = Elasticsearch()
		client.index(index="bitcoin_index", doc_type='bitcoin_article',\
					body=json_article)
					
	except Exception as ex:
		print("unable to save_news_to_eslastic_search: ex = ", ex)
		print(json_article)

def check_if_article_exists(title):
	
	try:
		client = Elasticsearch()
		response = client.search(index="bitcoin_index",
					body={
						"query": {
							"match_phrase": {
								"title": title
							}
						}
					})
					
		return response['hits']['total'] > 0
	except:
		pass