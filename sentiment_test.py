import re

def extract():
	with open("title.txt", "r") as file:
		f = file.readlines()

	
	for sentence in f:
		titles.append(sentence.replace('\n', ''))


def rate():
	for title in titles:
		print(title)
		x = input("Rating: ")
		ratings.append(x)

def write_ratings():
	with open("ratings.txt", "w") as file:
		for i, j in zip(titles, ratings):
			file.write(f"{i} {j}\n")


if __name__ == "__main__":
	
	titles = []
	ratings = []
	
	extract()
	rate()
	write_ratings()