from elasticsearch import Elasticsearch


def create_index():
	client = Elasticsearch()

	mapping = \
	{
		"settings": {
			"number_of_shards": 5,
			"number_of_replicas": 1,
		},
		
		"mappings": {
			"bitcoin_article": {
			"properties": {
				"title": { "index": "not_analyzed", "type": "text", 
					"fields": { "keyword": { "type": "keyword", "ignore_above": 256 }}},
				"keywords": { "index": "not_analyzed", "type": "keyword",
					"fields": { "keyword": { "type": "keyword", "ignore_above": 256 }}},
				"summary": { "index": "not_analyzed", "type": "text",
					"fields": { "keyword": { "type": "keyword", "ignore_above": 256 }}},
				"authors": { "index": "not_analyzed", "type": "text" ,
					"fields": { "keyword": { "type": "keyword", "ignore_above": 256 }}},
				"publish_date": { "index": "not_analyzed", "type": "date", 
						"format": "yyyy-MM-dd HH:mm:ss" },
				"link": { "index": "not_analyzed", "type": "text",
					"fields": { "keyword": { "type": "keyword", "ignore_above": 256 }}},
				"text": { "index": "not_analyzed", "type": "text",
					"fields": { "keyword": { "type": "keyword", "ignore_above": 256 }}},
				"blob_title": { "index": "not_analyzed", "type": "float" },
				"blob_summary": { "index": "not_analyzed", "type": "float" },
				"blob_full_text": { "index": "not_analyzed", "type": "float" },
				"vader_title": { "index": "not_analyzed", "type": "float" },
				"vader_summary": { "index": "not_analyzed", "type": "float" },
				"vader_full_text": { "index": "not_analyzed", "type": "float" },
				
			}}
		}
	}

	client.indices.create(index='bitcoin_index', body= mapping)

if __name__ == "__main__":

	create_index()




