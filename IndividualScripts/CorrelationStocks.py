import math
import numpy as np
import yfinance as yf

#Initialize data
data = {}
cov = []
var = []
cor = []
daily_returns = []

# Ask user to input
while True:
    stock = input("Enter your primary stock ticker symbol:")
    try:
        if stock == "Q": break
        stock_data = yf.download(stock, period="1y").resample("D").last()
        #stock = yf.Ticker(stock).info['longName'].split(",")[0]
        data[f'{stock}'] = stock_data
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")

while True:
    stocks = input("Enter your secondary stock ticker symbols(split with \" \"):").split(" ")
    try:
        if stocks == "Q": break
        for i in stocks:
            if i:
                current = i
                #current_name = yf.Ticker(i).info['longName'].split(",")[0]
                if current not in data.keys():
                    current_data = yf.download(i, period="1y").resample("D").last()
                    data[f'{current}'] = current_data
                else:
                    print(f'{i}'" is already loaded in data")
            else:
                current = "No input"
        break
    except:
        print(f'{current}'" is invalid")
        print("Or type Q to quit")

for i, key in enumerate(data):
    daily_returns.append([_ * 100 for _ in data[key]['Adj Close'].pct_change() if not math.isnan(_)])


for i, key in enumerate(data):
    cov.append(np.cov(daily_returns[0], daily_returns[i])[0][1])
    var.append(np.var(daily_returns[i]))
    cor.append(cov[i]/(math.sqrt(var[0])*math.sqrt(var[i])))
    print("The correlation between "f'{stock}'" and "f'{key}'": "f'{cor[i]}')