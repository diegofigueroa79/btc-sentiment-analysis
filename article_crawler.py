import requests
from newspaper import Article, Config



def get_news(article_url, news_date):
	
	try:
		article = Article(article_url)
		article.download()
		article.parse()
		article.nlp()
		
		if(article.title == "Are you a robot?"):
			print("robot identified")
			return
		else:
			return dict(article=article, news_date=news_date)
		
		
	except Exception as ex:
		print("newspaper could not download")
		return