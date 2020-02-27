import pandas as pd
from elastcisearch import Elasticsearch
import matplotlib.pyplot as plt


btc = pd.read_csv("BTC-USD.csv")
btc = btc[285:365]
btc_dates = [item for item in btc['Date']]
btc_price = [item for item in btc['Close']]

# plot for the bitcoin price
#plt.plot(btc[285:]['Date'], btc[285:]['Close'])
#plt.show()

# code for aggregating the number of documents per day
index = "bitcoin_index"
# this dictionary will call for a query
query = { 
	"query" : {
		"match_all" : {}
	}
}
# this dictionary will call for a bucket aggregation
# bucket aggregations only list document counts, Buckets simply
# collect documents based on a criteria, which means the only statistic they
# possess is a document count
aggregation = {
	"aggs" : { # this is the key that will tell es what operation we're doing
		"months" : { # this is just the name of our aggregation
			"date_histogram": { # this is telling es the type of aggregation
				"field" : "publish_date",
				"interval": "month"
			}
		}
	}
}

# metric aggregations are for when you want to calculate a values
# based on fields in the document, like the average price or total revenue
# metrics are simple mathematical operations, like min, max, avg, sum, etc

# here is an example of a pipeline aggregation, where the buckets from the
# first bucket aggregation, are the input for the nested metric aggregation.
# the metric aggregation is nested within every bucket from the bucket aggregation
pipeline_aggs = {
	"aggs": {
		"days": {
			"date_histogram": {
				"field": "publish_date",
				"interval": "day"
			},
			"aggs": {
				"vader_avg": {
					"avg": {"field": "vader_title"}
				}
			}
		}
	}
}

# bucket aggregations can also be of type date range
# these buckets are specifically for doing math operations with the date format
range = {
	"aggs": {
		"my_range": {
			"date_range": {
				"field": "publish_date",
				"ranges": {
					"from": "2019-12-01 00:00:00", "to" : "2020-02-19 00:00:00"
				}
			}
		}
	}
}


