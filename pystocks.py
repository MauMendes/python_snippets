#pip install yfinance
#C:\Python38\Scripts\pip.exe install yfinance

import yfinance as yf

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#info on the company
print(tickerData.info)

#info on the company calendar
print(tickerData.calendar)

#get recommendation data for ticker
print(tickerData.recommendations)

#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1mo', start='2020-1-1', end='2021-1-1')
tickerDf = tickerData.history(period='1y', interval='1mo')

#see your data
print(tickerDf)