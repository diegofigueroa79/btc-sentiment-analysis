from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

sentences = [
	"This is awesome!!!",
	"This is BAD!!!",
	"This is Boring!!!",
	"This is expensive",
	"This is Very expensive",
	"This is NOT safe",
	"This is safe",
	"This is VERY safe",
	"I like this",
	"We love this",
	"iPhone is a great product",
	"Their leader cannot work at night",
	"I hate final exams",
	"Kim is stupid",
	"we feel depressed",
]

for sentence in sentences:
	tb = TextBlob(sentence)
	print()
	print(tb)
	print("TextBlob analysis: ", tb.sentiment.polarity)
	ss = sia.polarity_scores(sentence)
	print("Vader analysis: ", ss['compound'])
	