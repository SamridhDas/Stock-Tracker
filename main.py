import yfinance as yf
import matplotlib.pyplot as plt
def analyse(ticker,days):

    stock=yf.Ticker(ticker)

    period=days+"d"
    data=stock.history(period=period)
    if data.empty:
        return None
    latest_open=data["Open"].iloc[-1]
    latest_close=data["Close"].iloc[-1]
    perchange=((latest_close-latest_open)/latest_open)*100
    per_sign=""
    if perchange>0:
        per_sign="+"
    else:
        per_sign=""
    moving_average=data["Close"].rolling(window=3).mean()

    average_close=data["Close"].mean()

    max_closing_price=data["Close"].max()
    min_closing_price=data["Close"].min()

    status=""
    if perchange>0:
        status="Bullish"
    elif perchange<0:
        status="Bearish"
    else:
        status="No Change"
    
    plot_graph(data,ticker,moving_average)
    
    return  latest_close, perchange,per_sign, average_close, max_closing_price, min_closing_price, status
        
def plot_graph(data,ticker,moving_average):
    plt.figure(figsize=(12,8))
    plt.grid()
    plt.plot(data.index,data["Close"],label="Closing Price")
    plt.plot(data.index,moving_average,label="3-day Moving Average")
    plt.legend()
    plt.title(f"{ticker} Closing Prices")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.ylabel("Closing Price")
    plt.savefig("static/stock_chart.png")
    plt.close()

    

    
                



    




