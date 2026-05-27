# Stock Tracker

A full-stack stock analysis web application built using Flask, Python, and financial market APIs.  
The application fetches live stock market data, performs analytical calculations, generates visualizations, and displays results through a modern responsive UI.

---

## Features

- Live stock market data retrieval using yfinance
- Percentage change calculation
- Bullish/Bearish market trend detection
- Average, highest, and lowest closing price analytics
- 3-day moving average analysis
- Dynamic stock price visualization with matplotlib
- Flask backend with HTML template rendering
- Responsive UI with CSS and Flexbox
- Error handling for invalid stock tickers
- Modular project structure
- Git/GitHub version control integration

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Flexbox
- yfinance API
- matplotlib
- Pandas
- Git/GitHub

---

## Project Structure

```text
stock_tracker/
│
├── static/
│   ├── stock_chart.png
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── main.py
├── requirements.txt
└── README.md