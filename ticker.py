from pandas_datareader import data as pdr 
import fix_yahoo_finance as yf 

yf.pdr_override() 
data=pdr.get_data_yahoo("SPY", start="2018-01-01", end="2018-04-30")