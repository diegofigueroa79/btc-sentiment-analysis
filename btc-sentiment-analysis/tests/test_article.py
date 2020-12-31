import pytest
from btc_sentiment_analysis.article import Article

@pytest.fixture
def supply_article_instance():
	article = Article(
		title="Bitcoin is crashing!",
		source="The WallStreet Journal",
		date="November 19, 2020",
		link="https://wallstreetjournal.com",
		text="Bitcoin is crashing once again. Everyone was right. Abandon ship."
	)
	return article

def test_vader_title_analysis(supply_article_instance):
	expected = 0.0
	actual = supply_article_instance.vader_analysis()['title']
	assert expected == actual, "Vader Title Analysis method failed."

def test_blob_title_analysis(supply_article_instance):
	expected = 0.0
	actual = supply_article_instance.blob_analysis()['title']
	assert expected == actual, "Blob Title Analysis method failed."

def test_vader_text_analysis(supply_article_instance):
	expected = -0.1468
	actual = supply_article_instance.vader_analysis()['text']
	assert expected == actual, "Vader Text Analysis method failed."

def test_blob_text_analysis(supply_article_instance):
	expected = 0.09523809523809523
	actual = supply_article_instance.blob_analysis()['text']
	assert expected == actual, "Blob Text Analysis method failed."
	