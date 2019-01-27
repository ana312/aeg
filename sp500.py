#Scrapes S&P Stock codes off Wikipedia page

import pandas as pd 

def SP500():
	SP500_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	SP500_data=SP500_data[1][1:][0]
	return SP500_data.tolist()
