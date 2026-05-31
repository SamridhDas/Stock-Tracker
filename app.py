from flask import Flask, render_template, request

from main import analyse,create_candlestick_chart
from flask import redirect

import yfinance as yf

app = Flask(__name__)
indian_stocks = [

    "TCS",
    "INFY",
    "RELIANCE",
    "HDFCBANK",
    "ICICIBANK",
    "SBIN",
    "WIPRO",
    "LT",
    "AXISBANK",
    "BAJFINANCE",
    "KOTAKBANK"
]


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/compare", methods=["GET", "POST"])
def compare():

    if request.method == "POST":

        ticker_input = request.form["ticker"]

        tickers = ticker_input.split(",")

        formatted_tickers=[]
        for ticker in tickers:
            ticker=ticker.strip().upper()
            if ticker in indian_stocks:
                ticker=ticker+".NS"
            formatted_tickers.append(ticker)
        tickers=formatted_tickers

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


@app.route("/solo", methods=["GET", "POST"])
def solo():

    if request.method == "POST":

        ticker = request.form["ticker"]

        ticker = ticker.strip().upper()
        if ticker in indian_stocks:
            ticker=ticker+".NS"

        return redirect(f"/stock/{ticker}")

    return render_template("solo.html")


@app.route("/stock/<ticker>")
def stock_page(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info
    data=stock.history(period="6mo")
    chart=create_candlestick_chart(data,ticker)

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
        stock_data=stock_data,chart=chart
    )


app.run(debug=True)