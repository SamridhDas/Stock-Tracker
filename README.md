# StockStalk 📈

StockStalk is a modern stock analytics platform built using Flask, Python, and yFinance. The platform allows users to compare multiple stocks, visualize relative market performance, and explore detailed individual stock analytics through interactive dashboards.

## Features

### Compare Stocks Dashboard

* Compare multiple stocks side-by-side
* Interactive normalized performance graphs
* Relative growth comparison
* Performance insights panel
* Best/Worst performer analytics
* Dynamic multi-stock visualization

### Individual Stock Analysis

* Dedicated stock analysis pages
* Company overview metrics
* Current price tracking
* 52-week high and low
* Market capitalization insights
* Dynamic routing for stock-specific pages

### Modern UI/UX

* Responsive dashboard layout
* Dark theme design
* Interactive hover animations
* SaaS-style landing page
* Feature showcase sections
* Structured navigation system

## Tech Stack

### Backend

* Python
* Flask
* yFinance

### Frontend

* HTML
* CSS
* Flexbox

### Data Visualization

* Matplotlib

## Architecture

The application follows a multi-page structure:

```text
/               → Landing Page
/compare        → Stock Comparison Tool
/stock/<ticker> → Individual Stock Analysis
```

## Current Analytics Features

* Relative stock growth normalization
* Comparative performance analysis
* Average growth calculations
* Most expensive stock tracking
* Market trend insights
* Performance summaries

## Planned Features

* Candlestick charts
* RSI indicators
* Volatility analysis
* Moving averages
* MACD analysis
* AI-powered stock insights
* Portfolio tracking
* Market news integration



## Learning Outcomes

This project helped develop skills in:

* Flask web development
* Dynamic routing
* Backend architecture
* Data visualization
* Dashboard UI design
* API integration
* Responsive layouts
* State/data structuring

## Installation

```bash
git clone <your-repository-link>

cd StockStalk

pip install -r requirements.txt

python app.py
```

## Future Vision

StockStalk is evolving into a complete financial analytics platform focused on:

* intelligent market visualization
* technical analysis
* AI-driven insights
* interactive financial dashboards
* scalable analytics systems
