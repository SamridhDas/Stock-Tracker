from flask import Flask,render_template,request
from main import analyse
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        ticker_input=request.form["ticker"]
        tickers=ticker_input.split(",")
        tickers=[ticker.strip().upper() for ticker in tickers]

        days=request.form["days"]

        result=analyse(tickers,days)
        if result is None:
            return render_template("result.html",error="Invalid Ticker")

        
        return render_template(
        "result.html",stock_summaries=result
       
        )
        

    
        

    return render_template("index.html")
app.run(debug="True")