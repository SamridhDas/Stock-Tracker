import yfinance as yf
import matplotlib.pyplot as plt

def analyse(tickers, days):

    all_data = {}

    for ticker in tickers:

        stock = yf.Ticker(ticker)

        data = stock.history(period=days + "d")

        if data.empty:
            return None

        all_data[ticker] = data

    stock_summaries=[]
    for ticker,data in all_data.items():
            latest_open = data["Open"].iloc[-1]

            latest_close = data["Close"].iloc[-1]

            perchange = ((latest_close - latest_open) / latest_open) * 100

            if perchange > 0:
                per_sign = "+"
            else:
                per_sign = ""

            

            average_close = data["Close"].mean()

            max_closing_price = data["Close"].max()

            min_closing_price = data["Close"].min()

            if perchange > 0:
                status = "Bullish"

            elif perchange < 0:
                status = "Bearish"

            else:
                status = "No Change"
            stock_summaries.append({

                "ticker": ticker,

                "latest_close": latest_close,

                "perchange": perchange,

                "per_sign": per_sign,

                "average_close": average_close,

                "max_closing_price": max_closing_price,

                "min_closing_price": min_closing_price,

                "status": status
            })




 

    plot_graph(all_data)
    return(stock_summaries)



def plot_graph(all_data):

    plt.figure(figsize=(12,8))

    plt.grid()

    for ticker, data in all_data.items():

        plt.plot(
            data.index,
            data["Close"],
            label=ticker
        )

    plt.legend()

    plt.title("Stock Comparison")

    plt.xlabel("Date")

    plt.ylabel("Closing Price")

    plt.xticks(rotation=45)

    plt.savefig("static/stock_chart.png")

    plt.close()