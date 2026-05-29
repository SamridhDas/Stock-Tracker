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

    stock_summaries = []

    for ticker, data in all_data.items():
        

        starting_price = data["Close"].iloc[0]
        ending_price = data["Close"].iloc[-1]

        total_growth = (
            (ending_price - starting_price)
            / starting_price
        ) * 100

        if total_growth > 0:
            per_sign = "+"
            status = "Bullish"

        elif total_growth < 0:
            per_sign = ""
            status = "Bearish"

        else:
            per_sign = ""
            status = "No Change"

        average_close = data["Close"].mean()

        max_closing_price = data["Close"].max()

        min_closing_price = data["Close"].min()

        stock_summaries.append({

            "ticker": ticker,

            "latest_close": ending_price,

            "total_growth": total_growth,

            "per_sign": per_sign,

            "average_close": average_close,

            "max_closing_price": max_closing_price,

            "min_closing_price": min_closing_price,

            "status": status
        })

    best_stock = max(
        stock_summaries,
        key=lambda stock: stock["total_growth"]
    )

    worst_stock = min(
        stock_summaries,
        key=lambda stock: stock["total_growth"]
    )

    average_change = sum(
        stock["total_growth"]
        for stock in stock_summaries
    ) / len(stock_summaries)

    most_expensive = max(
        stock_summaries,
        key=lambda stock: stock["latest_close"]
    )

    plot_graph(all_data)

    return {

        "stock_summaries": stock_summaries,

        "insights": {

            "best_stock": best_stock,

            "worst_stock": worst_stock,

            "average_change": average_change,

            "most_expensive": most_expensive
        }
    }


def plot_graph(all_data):

    plt.figure(figsize=(12, 8))

    plt.grid()

    for ticker, data in all_data.items():

        normalized_prices = (
            data["Close"] / data["Close"].iloc[0]
        ) * 100

        plt.plot(
            data.index,
            normalized_prices,
            label=ticker
        )

    plt.legend()

    plt.title("Relative Stock Performance")

    plt.xlabel("Date")

    plt.ylabel("Normalized Growth")

    plt.xticks(rotation=45)

    plt.savefig("static/stock_chart.png")

    plt.close()

