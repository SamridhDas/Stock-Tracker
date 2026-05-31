# StockStalk 📈

StockStalk is a modern stock analytics platform built using Flask, Python, Plotly, and yFinance. The platform allows users to compare multiple stocks, explore technical analysis indicators, and visualize market trends using interactive financial dashboards.

---

# Features

## Multi-Stock Comparison

* Compare multiple stocks side-by-side
* Relative growth normalization charts
* Performance insights dashboard
* Best and worst performer analytics
* Average market growth calculations
* Interactive comparison visualizations

---

## Individual Stock Analysis

* Dedicated stock analysis pages
* Interactive candlestick charts
* Moving average overlays (20-Day & 50-Day)
* Company overview metrics
* Market capitalization tracking
* 52-week high and low analysis
* Technical analysis focused dashboards

---

## Modern UI/UX

* SaaS-inspired landing page
* Responsive dashboard layouts
* Dark-themed financial interface
* Interactive hover animations
* Feature-based navigation system
* Structured multi-page architecture

---

# Technical Analysis Features

## Candlestick Charts

Visualize market price movement using interactive candlestick charts displaying:

* Open price
* Close price
* High price
* Low price

These charts help identify:

* market momentum
* bullish and bearish trends
* volatility
* reversal patterns

---

## Moving Averages

StockStalk currently supports:

* 20-Day Moving Average
* 50-Day Moving Average

These indicators help smooth market noise and identify:

* trend direction
* momentum shifts
* support and resistance zones

---

# Tech Stack

## Backend

* Python
* Flask
* yFinance

## Frontend

* HTML
* CSS
* Flexbox

## Data Visualization

* Matplotlib
* Plotly

---

# Application Architecture

```text
/               → Landing Page
/compare        → Multi-Stock Comparison
/result         → Comparison Results Dashboard
/solo           → Individual Analysis Search
/stock/<ticker> → Technical Analysis Dashboard
```

---

# Supported Markets

## US Stocks

Examples:

* AAPL
* TSLA
* GOOGL

## Indian Stocks

StockStalk automatically supports NSE tickers including:

* TCS
* INFY
* RELIANCE
* HDFCBANK

through automatic `.NS` conversion for Yahoo Finance integration.

---

# Planned Features

* RSI (Relative Strength Index)
* Volatility analysis
* MACD indicators
* Volume analytics
* Bollinger Bands
* AI-generated market insights
* Portfolio tracking
* News sentiment analysis
* Watchlists

---

# Learning Outcomes

This project helped develop skills in:

* Flask web development
* Multi-page routing architecture
* Interactive financial visualization
* Technical analysis implementation
* Backend data structuring
* Plotly integration
* Responsive UI design
* API-driven applications
* Financial analytics engineering

---

# Installation

```bash
git clone <your-repository-link>

cd StockStalk

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python app.py
```

---

# Future Vision

StockStalk is evolving into a full financial analytics platform focused on:

* interactive technical analysis
* intelligent financial visualization
* scalable dashboard systems
* AI-powered market insights
* professional-grade stock research tools

```
```
