# btc-sentiment-analysis
Small Python package for gathering news articles and performing basic bitcoin sentiment analysis.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install btc-sentiment-analysis.

```bash
pip install btc-sentiment-analysis
```

## Usage
This python package contains python scripts for gathering news articles on the topic "Bitcoin." An XML file provided by a Google news RSS Feed, is parsed for all published news articles on "Bitcoin." The urls of the published articles are visited and scraped for all usable content such as title, article, published date, etc.

```python
from btc_sentiment_analysis import scrape_btc_news, visualize

articles = scrape_btc_news() # returns a list of Article objects
visualize(articles) # receives list of Article objects as an argument, displays simple seaborn violin plot
```
The function scrape_btc_news() crawls for BTC articles on the web, scrapes important information, and creates Article objects for each news Article.
Article objects contain attributes such as title, text, news source, publication date, and link. Article objects also contain two methods.
The vader_analysis method uses the Natural Language Toolkit (nltk) library to return the sentiment of the title and text of the article as a dict type.
The blob_analysis method uses the Text Blob (textblob) library to return the sentiment of the title and text of the article as a dict type.

```python
class Article:
	
	def __init__(self, title, source, date, link, text):
		...
	
	def vader_analysis(self):
		...
		return {'title': title_sentiment, 'text': text_sentiment}
	
	def blob_analysis(self):
		...
		return {'title': title_sentiment, 'text': text_sentiment}
```
The function visualize simply plots an example Violin Plot using seaborn. Visualize takes any list of Article objects and returns a seaborn violin plot
showing the distribution of the sentiment analysis for Article.title and Article.text using nltk's Vader, and Text Blob.

![Bitcoin_Violin_Plot](https://github.com/diegofigueroa79/btc-sentiment-analysis/blob/master/btc_violinplot.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
