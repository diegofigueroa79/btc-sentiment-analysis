import json
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

nltk_predictions = []
blob_predictions = []
bull_words = []
bear_words = []

with open("bull_words.txt", "r") as read_file:
	bull_words = read_file.readlines()

bull_words = [word.replace("\n", "") for word in bull_words]

with open("bear_words.txt", "r") as read_file:
	bear_words = read_file.readlines()
	
bear_words = [word.replace("\n", "") for word in bear_words]

with open("ratings_data.json", "r") as read_file:
	data = json.load(read_file)

sentences = [sentence.lower() for sentence in data['sentences']]
ratings = [float(rating) for rating in data['only_ratings']]

def calc_bias(sentence):
	bias = 0
	for word in bull_words:
		if word in sentence:
			bias = 1
			return bias
	for word in bear_words:
		if word in sentence:
			bias = -1
			return bias
	return bias

for sentence in sentences:
	score = 0
	ss = sia.polarity_scores(sentence)
	bias = calc_bias(sentence)
	score = ss['compound'] + bias
	if score > 1:
		nltk_predictions.append(1)
	elif score < -1:
		nltk_predictions.append(-1)
	else:
		nltk_predictions.append(score)

for sentence in sentences:
	score = 0
	tb = TextBlob(sentence)
	bias = calc_bias(sentence)
	score = tb.sentiment.polarity + bias
	if score > 1:
		blob_predictions.append(1)
	elif score < -1:
		blob_predictions.append(-1)
	else:
		blob_predictions.append(score)

def mean_square(ratings, predictions):
	summation = 0
	n = len(ratings)
	for i in range(0, n):
		difference = ratings[i] - predictions[i]
		squared_difference = difference**2
		summation += squared_difference
	MSE = summation/n
	return MSE

vader_results = mean_square(ratings, nltk_predictions)
textblob_results = mean_square(ratings, blob_predictions)

print("Vader results: ", vader_results)
print("TextBlob results: ", textblob_results)

for i in range(0, 20):
	print(sentences[i])
	print(ratings[i])
	print("nltk: ", nltk_predictions[i])
	print("tblob: ", blob_predictions[i])
	print("\n")