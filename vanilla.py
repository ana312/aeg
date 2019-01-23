from pandas_datareader import data as pdr 
from sp500 import SP500
from ticker import SP_data
import fix_yahoo_finance as yf 
import pandas as pd
import numpy as np
import datetime

def exp_return(data):
	operable_data=data.Open.values
	exp_return=np.mean(operable_data, axis=0)
	return exp_return

def covmatrix(data):
	operable_data=data.Open.values
	cov_matrix=np.cov(operabe_data.T)
	return cov_matrix
