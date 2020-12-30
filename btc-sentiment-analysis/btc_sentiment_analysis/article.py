from analyzers import vader_analyze, blob_analyze

class Article:
	
	def __init__(self, title, source, date, link, text):
		self.title = title
		self.source = source
		self.date = date
		self.link = link
		self.text = text
	
	def vader_analysis(self):
		title_sentiment = vader_analyze(self.title)
		text_sentiment = vader_analyze(self.text)
		return {'title': title_sentiment, 'text': text_sentiment}
	
	def blob_analysis(self):
		title_sentiment = blob_analyze(self.title)
		text_sentiment = blob_analyze(self.text)
		return {'title': title_sentiment, 'text': text_sentiment}
	
	
	