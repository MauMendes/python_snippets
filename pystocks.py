#pip install yfinance
#C:\Python38\Scripts\pip.exe install yfinance

import yfinance as yf

def getStock(tickerSymbol):
    print(tickerSymbol)
    #define the ticker symbol
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #info on the company
    #print(tickerData.info)
    #print("###########################")

    #info on the company calendar
    #print(tickerData.calendar)
    #print("###########################")

    #get recommendation data for ticker
    #print(tickerData.recommendations)
    #print("###########################")

    #print(tickerData.dividends)
    #print("###########################")

    #print(tickerData.actions)
    #print("###########################")

    #print(tickerData.financials)
    #print("###########################")

    #print(tickerData.quarterly_financials)
    #print("###########################")

    #print(tickerData.major_holders)
    #print("###########################")


    #get the historical prices for this ticker
    #tickerDf = tickerData.history(period='1mo', start='2020-1-1', end='2021-1-1')
    tickerDf = tickerData.history(period='1d', interval='1d')
    #see your data
    print(tickerDf)
    print("###################################################################")

stocks = ['AIR.NZ', 'KMD.NZ', 'KFL.NZ', 'AAPL', 'MSFT', 'VTI', 'SRET']
for stock in stocks:
    getStock(stock)