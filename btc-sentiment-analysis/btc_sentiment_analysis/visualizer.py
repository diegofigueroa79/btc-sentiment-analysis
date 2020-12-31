import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize(articles_ls):
	df = get_dataframe(articles_ls)
	ax = sns.violinplot(data=df)
	ax.set_title("Bitcoin Sentiment Analysis")
	ax.set_ylabel("Normalized Sentiment")
	plt.show()

def get_dataframe(articles_ls):
	vader_title = []
	vader_text = []
	blob_title = []
	blob_text = []
	
	for article in articles_ls:
		v_a = article.vader_analysis()
		b_a = article.blob_analysis()
		vader_title.append(v_a['title'])
		vader_text.append(v_a['text'])
		blob_title.append(b_a['title'])
		blob_text.append(b_a['text'])
	
	data = { 
		'vader_title': vader_title, 
		'vader_text': vader_text, 
		'blob_title': blob_title, 
		'blob_text': blob_text
	}
	
	df = pd.DataFrame(data)
	
	return df
