# Flask Stock Tracker

A Flask-based stock analysis web application that fetches real-time stock market data using yfinance, performs financial analysis, and visualizes stock trends with matplotlib.

## Features

- Real-time stock data fetching using yfinance
- Web interface built with Flask
- Dynamic stock analysis using user input
- Daily percentage change calculation
- Bullish/Bearish market status detection
- Average closing price calculation
- Highest and lowest closing price tracking
- Moving average trend analysis
- Stock price graph generation using matplotlib
- HTML template rendering with Flask

## Technologies Used

- Python
- Flask
- HTML
- yfinance
- matplotlib
- Git/GitHub

## Concepts Learned

- Flask web development
- Backend/frontend architecture
- GET and POST requests
- HTML templates with Jinja
- Form handling in Flask
- APIs and real-time data fetching
- Data visualization
- Rolling averages
- Financial analytics
- Time-series plotting
- Modular programming
- Git version control

## Project Structure

```text
stock_tracker/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── stock_chart.png
│
└── templates/
    ├── index.html
    └── result.html
```

## Installation

Clone the repository:

```bash
git clone <your-repo-link>
cd stock_tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python3 app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

## Usage

1. Enter a stock ticker symbol (example: AAPL)
2. Enter number of days for analysis
3. Click the Analyze button
4. View stock analytics and generated visualizations

## Future Improvements

- Interactive charts
- Improved UI with CSS
- Display graphs directly on webpage
- Multiple stock comparison
- Portfolio tracking
- AI-powered stock insights
- Error handling for invalid tickers

## Author

Built by Samridh Das as part of learning Python, Flask, APIs, and full-stack development.