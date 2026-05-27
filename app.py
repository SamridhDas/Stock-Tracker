from flask import Flask,render_template,request
from main import analyse
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        ticker=request.form["ticker"]
        days=request.form["days"]
        result=analyse(ticker,days)
        if result is None:
            return render_template("result.html",error="Invalid Ticker")

        latest_close, perchange,per_sign, average_close, max_closing_price, min_closing_price, status=result
        return render_template(
        "result.html",
        latest_close=latest_close,
        perchange=perchange,
        per_sign=per_sign,
        average_close=average_close,
        max_closing_price=max_closing_price,
        min_closing_price=min_closing_price,
        status=status
        )
        

    
        

    return render_template("index.html")
app.run(debug="True")