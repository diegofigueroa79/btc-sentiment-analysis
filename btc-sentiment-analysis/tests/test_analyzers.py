import pytest
from btc_sentiment_analysis.analyzers import vader_analyze, blob_analyze

@pytest.fixture
def supply_negative_string():
	negative = "I hate you"
	return negative

def test_vader_negative_analysis(supply_negative_string):
	expected = -0.5719
	actual = vader_analyze(supply_negative_string)
	assert expected == actual, "Vader Negative Analysis method failed."

def test_blob_negative_analysis(supply_negative_string):
	expected = -0.8
	actual = blob_analyze(supply_negative_string)
	assert expected == actual, "Blob Negative Analysis method failed."
	