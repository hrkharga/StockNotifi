import pandas
from yahoo_finance import Share
df = pandas.read_csv('stockdata.csv')
#dp = pandas.read_csv('stocks.csv',names=['pTicker'])
#tickers = dp.pTicker.values
tickers = ['Yahoo! Inc.', 'Apple Inc.', 'Affymax, Inc.']
symbols = []
for i in range(len(tickers)):
    test = df[df.Name == tickers[i]]
    if not (test.empty):
        symbols.append(list(test.Ticker.values)[0])
for stocks in symbols:
    stock = Share(stocks)
    print stocks + ' : ' + stock.get_price()
