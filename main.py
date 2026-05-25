import yfinance as yf
import matplotlib.pyplot as plt
ticker=input("Enter stock ticker: ").upper()
stock=yf.Ticker(ticker)
days=input("Enter Number of Days: ")
period=days+"d"
data=stock.history(period=period)
latest_open=data["Open"].iloc[-1]
latest_close=data["Close"].iloc[-1]
perchange=((latest_close-latest_open)/latest_open)*100
per_sign=""
if perchange>0:
    per_sign="+"
else:
    per_sign=""
moving_average=data["Close"].rolling(window=3).mean()
print("===== STOCK ANALYSIS =====")
print("--------------------------")
print(f"\nTicker: {ticker}\n")
print("--- PRICE DATA ---")
print(f"Latest Price: ${latest_close:.2f}")
print("Daily Change: "+per_sign+f"{perchange:.2f}%\n")
print("--- ANALYTICS ---")
average_close=data["Close"].mean()
print(f"Average Closing Price: ${average_close:.2f}")
max_closing_price=data["Close"].max()
min_closing_price=data["Close"].min()
print(f"Highest Closing Price: ${max_closing_price:.2f}")
print(f"Lowest Closing Price: ${min_closing_price:.2f}")
status=""
if perchange>0:
    status="Bullish"
elif perchange<0:
    status="Bearish"
else:
    status="No Change"
print(f"\nMarket Status: {status}")
plt.figure(figsize=(12,8))
plt.grid()
plt.plot(data.index,data["Close"],label="Closing Price")
plt.plot(data.index,moving_average,label="3-day Moving Average")
plt.legend()
plt.title(f"{ticker} Closing Prices")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Closing Price")
plt.savefig("stock_chart.png")



