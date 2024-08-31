#@author: GaloisField
#@desc: Import yahoo finance data and save it in tuples
#       Extracting functions

import yfinance as yf

# Save the data in a list of tuples
def extract_tuples(data):    
    # Extract and print specific columns
    high = data['High']
    low = data['Low']
    open_ = data['Open']
    close = data['Close']
    
    time = data.index

    n = len(high)

    X = []

    for i in range(n):
        vector = (high.iloc[i], low.iloc[i], open_.iloc[i], close.iloc[i])
        t = time[i]
        candle = [t, vector]
        X.append(candle)

    return X



def extract(ticker, start, end):
    # Download historical data from Yahoo Finance
    data = yf.download(ticker, start=start, end=end)
    data = data.round(4)

   # Save the data in a list of tuples
    X = extract_tuples(data)
    return X

def print_data(X):
    print("\nData in tuples:")
    print(str(X[:5]))

def compute_color(vector):
    color = ""
    open_ = vector[2]
    close = vector[3]
    if open_ < close:
        color = '💚'
    else:
        color = '🔴'
    return color

#X = extract('BTC-EUR', '2024-08-01', '2024-08-31')

#print_data(X)

#    print("\nHigh Prices:", len(high))
#    print(high.head())

 #   print("\nLow Prices:",len(low))
  #  print(low.head())

   # print("\nOpen Prices:")
   # print(open_.head())

   # print("\nClose Prices:")
   # print(close.head())

 
