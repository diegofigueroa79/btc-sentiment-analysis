from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from textblob import TextBlob

client = Elasticsearch()

s = Search(using=client, index="news_data")

date = "2019-09"

q = Q('bool', must=[Q('match_phrase', publish_date=date), \
					Q('match', Symbol='HUBS')])

s = s.query(q)

response = s.execute()


full_text = response[2].text
summary = response[2].summary

sentences = []
full_text_sentences = []
full_text_sentences = sent_tokenize(full_text)
sentences = sent_tokenize(summary)
textblob_average = 0
vader_average = 0
full_text_blob_average = 0
full_text_vader_average = 0

sia = SentimentIntensityAnalyzer()

for sentence in sentences:
	tb = TextBlob(sentence)
	ss = sia.polarity_scores(sentence)
	print()
	print(tb)
	print("TextBlob Analysis: ", tb.sentiment.polarity)
	print("Vader Analysis: ", ss['compound'])
	textblob_average += tb.sentiment.polarity
	vader_average += ss['compound']

for sentence in full_text_sentences:
	tb = TextBlob(sentence)
	ss = sia.polarity_scores(sentence)
	full_text_blob_average += tb.sentiment.polarity
	full_text_vader_average += ss['compound']

print()
print("TexBlob Summary Average: ", textblob_average/len(sentences))
print("Vader Summary Average: ", vader_average/len(sentences))
print()
print("TexBlob Full Text Average: ", full_text_blob_average/len(full_text_sentences))
print("Vader Full Text Average: ", full_text_vader_average/len(full_text_sentences))