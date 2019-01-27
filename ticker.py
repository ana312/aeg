#Returns SP500 Data from Yahoo over j-day interval from today
#Takes j, no. of days data to return 

from pandas_datareader import data as pdr 
from sp500 import SP500
import fix_yahoo_finance as yf 
import pandas as pd
import numpy as np
import datetime


def SP_data(j):
	yf.pdr_override()

	end_date = datetime.date.today() 
	start_date = end_date + datetime.timedelta(-j)

	data=pdr.get_data_yahoo(SP500(), start=start_date.isoformat(), end=end_date.isoformat())
	return data
	#data.to_csv('data.csv', index=False)


