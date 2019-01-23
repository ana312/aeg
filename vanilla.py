from pandas_datareader import data as pdr 
from sp500 import SP500
import fix_yahoo_finance as yf 
import pandas as pd
import numpy as np
import datetime

def SP_data():
	yf.pdr_override()

	end_date = datetime.date.today() 
	start_date = end_date + datetime.timedelta(-30)

	data=pdr.get_data_yahoo(SP500(), start=start_date.isoformat(), end=end_date.isoformat())
	return data
	#data.to_csv('data.csv', index=False)

def exp_return(data):
	operable_data=data.Open.values
	exp_return=np.mean(operable_data, axis=0)
	return exp_return

def covmatrix(data):
	operable_data=data.Open.values
	cov_matrix=np.cov(operabe_data.T)
	return cov_matrix
