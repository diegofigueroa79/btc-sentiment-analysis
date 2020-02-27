import pandas as pd
from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt
import numpy as np

btc = pd.read_csv("BTC-USD.csv")
btc = btc[285:365]
btc_dates = [item for item in btc['Date']]
btc_price = [item for item in btc['Close']]

index = 'bitcoin_index'
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

es = Elasticsearch()
results = es.search(index=index, body=pipeline_aggs)

bucket = results['aggregations']['days']['buckets']
bucket = [item for item in bucket[16:]]
bucket = [item for item in bucket[:80]]
doc_counts = [item['doc_count'] for item in bucket]
vader_avgs = [item['vader_avg']['value'] for item in bucket]
vader = []
for item in vader_avgs:
	if item == None:
		vader.append(0.0)
	else:
		vader.append(item)

"""
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_ylabel('document_count', color=color)
ax1.plot(btc_dates, doc_counts, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax1.fill_between(btc_dates, doc_counts,
facecolor='b', alpha=0.25)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_xlabel('days (Dec - Feb)')
ax2.set_ylabel('price', color=color)
ax2.plot(btc_dates, btc_price, color=color, linewidth=2)

fig.tight_layout()
plt.show()
"""

#########################


fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_ylabel('sentiment', color=color)
ax1.plot(btc_dates, vader, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax1.fill_between(btc_dates, vader,
facecolor='g', alpha=0.5)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_xlabel('days (Dec - Feb)')
ax2.set_ylabel('price', color=color)
ax2.plot(btc_dates, btc_price, color=color)

fig.tight_layout()
plt.show()


