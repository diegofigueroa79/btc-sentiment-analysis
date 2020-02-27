import json
from date_converter import convert_date
from bitcoin_sentiment import *
from elastic_search_save import save_to_elasticsearch, check_if_article_exists


def write_json(article_dict):
	
	new_date = convert_date(article_dict['news_date'])
	article_object = article_dict['article']
	
	blob_title = blob_analyze(article_object.title)
	blob_summary = blob_analyze(article_object.summary)
	blob_full_text = blob_analyze(article_object.text)
	
	vader_title = vader_analyze(article_object.title)
	vader_summary = vader_analyze(article_object.summary)
	vader_full_text = vader_analyze(article_object.text)
	
	row = {}
	
	try:
		row['title'] = article_object.title
		row['keywords'] = article_object.keywords
		row['summary'] = article_object.summary
		row['authors'] = article_object.authors
		row['publish_date'] = new_date
		row['link'] = str(article_object.url)
		row['text'] = article_object.text
		row['blob_title'] = blob_title
		row['blob_summary'] = blob_summary
		row['blob_full_text'] = blob_full_text
		row['vader_title'] = vader_title
		row['vader_summary'] = vader_summary
		row['vader_full_text'] = vader_full_text
		
		if(check_if_article_exists(article_object.title)):
			print("This article is already in the db")
		else:
			save_to_elasticsearch(json.dumps(row))
	
	except Exception as ex:
		print("Unable to write json object: ", article_object.url)