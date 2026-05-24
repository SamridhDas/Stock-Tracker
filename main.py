import yfinance as yf
ticker=input("Enter stock ticker: ")
stock=yf.Ticker(ticker)
data=stock.history(period="1d")
latest_open=data["Open"].iloc[-1]
latest_close=data["Close"].iloc[-1]
perchange=((latest_close-latest_open)/latest_open)*100
print(ticker)
print(f"Latest Price: {latest_close:.2f}")
print(f"Daily Change: {perchange:.2f}%")
if perchange>0:
    print("Green")
else:
    print("Red")

