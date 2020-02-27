import re


def convert_date(string):

	new_string = string[5:25]

	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

	date = ''
	i = 0
	while (i < len(months)):
		
		if( new_string[3:6] == months[i] ):
		
			if(i < 10):
				replace = "0" + str(i + 1)
			else:
				replace = str(i + 1)
				
			pattern = '[a-zA-Z][a-zA-Z][a-zA-Z]'
			date = re.sub(pattern, replace, new_string)
			break
		else: i += 1
	
	replace_year_with = "-" + date[:2] + " "
	replace_day_with = date[6:10] + "-"
	
	day_pattern = '^..\s'
	year_pattern = '\s\d..\d\s'
	
	date = re.sub(day_pattern, replace_day_with, date)
	date = re.sub(year_pattern, replace_year_with, date)

	return date