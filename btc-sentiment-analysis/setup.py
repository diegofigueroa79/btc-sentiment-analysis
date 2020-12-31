from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='btc-sentiment-analysis',
	version='0.0.2',
	autho='Diego Figueroa',
	author_email='diegofigueroa79@gmail.com',
	description='A small sentiment analysis library for bitcoin',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/diegofigueroa79/btc-sentiment-analysis',
	packages=find_packages(include=['btc_sentiment_analysis', 'btc_sentiment_analysis.*']),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	install_requires=[
		'beautifulsoup4',
		'lxml',
		'matplotlib',
		'newspaper3k',
		'nltk',
		'pandas',
		'requests',
		'seaborn',
		'textblob',
	],
	extras_require={
		'dev': ['pytest'],
	},
) 
