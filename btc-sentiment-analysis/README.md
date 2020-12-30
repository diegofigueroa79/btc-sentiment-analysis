# btc-sentiment-analysis
Gathering news articles for bitcoin market sentiment analysis


This repository contains python scripts for gathering news articles on the topic "Bitcoin." An XML file provided by a Google news RSS Feed, is parsed for all published news articles on "Bitcoin." The urls of the published articles are visited and scraped for all usable content such as title, article, published date, etc. The data is then cleaned and serialized into JSON in order to upload the objects onto an Elasticsearch index. After gathering a substantial amount of news articles over time, the data is then analyzed and charted against the bitcoin price. This is doing using Natural Language Processing techniques provided by TextBlob, Natural Language Toolkit, and analysis tools provided by Elasticsearch.

Most of these scripts cannot be run because the months of published article data are NOT provided. However, you can read these scripts for your own purpose of writing your own sentiment analysis project.

![Bitcoin Activity vs Price](https://github.com/diegofigueroa79/btc-sentiment-analysis/blob/master/activity_vs_price.png)
