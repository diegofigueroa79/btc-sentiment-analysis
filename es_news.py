from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

import matplotlib.pyplot as plt

client = Elasticsearch()

article_count = []
i = 1

while( i < 11 ):

	date = "2019"
	
	if(i == 10):
		date += "-" + str(i)
	else:
		date += "-0" + str(i)
	
	
	s = Search(using=client, index="news_data")
	
	q = Q('bool', must=[Q('match_phrase', publish_date=date), \
						Q('match', Symbol="HUBS")])
	
	s = s.query(q)
	s.execute()
	article_count.append(s.count())
	
	i += 1

print(article_count)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct"]
plt.plot(months, article_count)
plt.xlabel('2019')
plt.ylabel('Featured Articles')
plt.title('HubSpot Inc.')
plt.show()