import requests
from bs4 import BeautifulSoup
from newspaper import Article
from . import article

def scrape_btc_news():
	
	# url of rss feed
	url = 'https://news.google.com/rss/search?q=bitcoin&hl=en-US&gl=US&ceid=US:en'
	response = requests.get(url)
	# parse xml and return all items
	soup = BeautifulSoup(response.content, 'xml')
	items = soup.findAll('item')
	
	# create dictionary list of each item's
	# title, link, date, and source
	news_items = []
	for item in items:
		link = item.find('link').text
		article_dict = {
			'title': item.find('title').text,
			'link': link,
			'date': item.find('pubDate').text,
			'source': item.find('source').text,
			'text': get_text(link),
		}
		news_items.append(article_dict)
	
	# clean data, remove None values
	news_items = [item for item in news_items if item['text'] != None]
	
	# create Article objects out of news_items
	articles = []
	for item in news_items:
		a = article.Article(
			title = item['title'],
			source = item['source'],
			date = item['date'],
			link = item['link'],
			text = item['text'],
		)
		articles.append(a)
	
	return articles

def get_text(article_url):
	try:
		article = Article(article_url)
		article.download()
		article.parse()
		
		if article.title == "Are you a robot?":
			print("Robot data returned. Skipping...")
			return
		else:
			return article.text
	
	except Exception as ex:
		print("Newspaper could not download article...")

