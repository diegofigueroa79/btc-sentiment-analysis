import json
from bitcoin_sentiment import vader_analyze, blob_analyze
from elasticsearch import Elasticsearch
from elastic_search_save import save_to_elasticsearch, check_if_article_exists



def stripData(entry):
	
	blob_title = blob_analyze(entry['_source']['title'])
	blob_summary = blob_analyze(entry['_source']['summary'])
	blob_full_text = blob_analyze(entry['_source']['text'])
	
	vader_title = vader_analyze(entry['_source']['title'])
	vader_summary = vader_analyze(entry['_source']['summary'])
	vader_full_text = vader_analyze(entry['_source']['text'])
	
	row = {}
	
	row['title'] = entry['_source']['title']
	row['keywords'] = entry['_source']['keywords']
	row['summary'] = entry['_source']['summary']
	row['authors'] = entry['_source']['authors']
	row['publish_date'] = entry['_source']['publish_date']
	row['link'] = entry['_source']['link']
	row['text'] = entry['_source']['text']
	row['blob_title'] = blob_title
	row['blob_summary'] = blob_summary
	row['blob_full_text'] = blob_full_text
	row['vader_title'] = vader_title
	row['vader_summary'] = vader_summary
	row['vader_full_text'] = vader_full_text
	
	return json.dumps(row)

def main():
	
	es = Elasticsearch()
	
	query = {
		"query": {
			"match_all": {}
		},
		"size": 200
	}
	
	resultados = es.search(index="bitcoin_news", body=query)
	
	entries = [hit for hit in resultados['hits']['hits']]
	
	entries = [entry for entry in entries if check_if_article_exists(entry['_source']['title']) == False]
	
	json_entries = [stripData(entry) for entry in entries]
	
	for entry in json_entries:
		save_to_elasticsearch(entry)


if __name__ == "__main__":
	
	main()