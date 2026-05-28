# Stock Tracker Dashboard

A full-stack stock market analytics dashboard built using Flask, Python, and financial market APIs.
The application fetches live market data, performs analytical calculations, generates dynamic visualizations, and presents insights through a responsive dashboard-style interface.

---

## Features

### Market Data & Analytics

* Live stock market data retrieval using yfinance
* Multi-stock comparison support
* Percentage change calculations
* Bullish/Bearish trend detection
* Average closing price analysis
* Highest and lowest closing price analytics
* Rolling moving average calculations

---

### Data Visualization

* Dynamic stock comparison graphs
* Multi-line comparative price visualization
* Real-time graph generation using matplotlib
* Dashboard-style analytics cards

---

### Web Application Features

* Flask backend with dynamic routing
* Jinja templating engine
* Dynamic rendering of stock analytics
* Error handling for invalid stock tickers
* Responsive UI with Flexbox
* Dark-themed dashboard interface

---

## Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* Flexbox
* Jinja Templates

### Data & Visualization

* yfinance API
* Pandas
* matplotlib

### Development Tools

* Git
* GitHub

---

## Project Architecture

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
```

---

## Current Functionality

Users can:

1. Enter multiple stock tickers
2. Choose analysis duration
3. Compare stock performance visually
4. View analytics for each stock individually
5. Analyze:

   * Latest price
   * Percentage change
   * Average closing price
   * Highest/lowest close
   * Market status
6. Generate comparative stock graphs dynamically

---

## Software Engineering Concepts Learned

### Backend Engineering

* Flask routing
* Request handling
* Dynamic data processing
* Modular application structure
* Error handling

### Frontend Engineering

* Responsive layouts
* Flexbox systems
* Dynamic template rendering
* Dashboard UI design

### Data Engineering

* Financial API integration
* Data transformation
* Dictionary/list-based data structures
* Comparative analytics

### Visualization

* Dynamic graph generation
* Multi-stock plotting
* Time-series visualization

### Development Workflow

* Git version control
* Incremental feature development
* Refactoring
* Architecture scaling

---

## Future Improvements

* Normalized stock performance comparison
* Interactive charts
* Candlestick visualizations
* Technical indicators (RSI, MACD, Volatility)
* Portfolio tracking
* User authentication
* Database integration
* Cloud deployment
* AI-powered market insights

---



## Author

Built by Samridh Das as part of a software engineering and financial analytics learning journey.
