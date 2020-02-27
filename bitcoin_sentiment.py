from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from textblob import TextBlob

def vader_analyze(text):
	sentences = []
	sentences = sent_tokenize(text)
	
	sent_sum = 0
	
	sia = SentimentIntensityAnalyzer()
	
	for sentence in sentences:
		ss = sia.polarity_scores(sentence)
		sent_sum += ss['compound']
	
	if (len(sentences) > 0):
		vader_average = sent_sum/len(sentences)
		return vader_average
	else:	
		return sent_sum
		

def blob_analyze(text):
	sentences = []
	sentences = sent_tokenize(text)
	
	sent_sum = 0
	
	for sentence in sentences:
		tb = TextBlob(sentence)
		sent_sum += tb.sentiment.polarity
	
	if (len(sentences) > 0):
		blob_average = sent_sum/len(sentences)
		return blob_average
	else:
		return sent_sum