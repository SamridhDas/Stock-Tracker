from flask import Flask, render_template, request

from main import analyse

import yfinance as yf

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/compare", methods=["GET", "POST"])
def compare():

    if request.method == "POST":

        ticker_input = request.form["ticker"]

        tickers = ticker_input.split(",")

        tickers = [
            ticker.strip().upper()
            for ticker in tickers
        ]

        days = request.form["days"]

        result = analyse(tickers, days)

        if result is None:

            return render_template(
                "compare.html",
                error="Invalid Ticker"
            )

        return render_template(
            "result.html",
            results=result
        )

    return render_template("compare.html")


@app.route("/stock/<ticker>")
def stock_page(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    stock_data = {

        "ticker": ticker,

        "company_name": info.get("longName"),

        "current_price": info.get("currentPrice"),

        "market_cap": info.get("marketCap"),

        "fifty_two_high": info.get("fiftyTwoWeekHigh"),

        "fifty_two_low": info.get("fiftyTwoWeekLow")
    }

    return render_template(
        "stock.html",
        stock_data=stock_data
    )


app.run(debug=True)