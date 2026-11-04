from flask import Flask, render_template, request
from data import get_prices_open
from main import send_daily_digest, check_exchange_open
import re
from db import init_db, add_subscriber, get_all_subscribers

init_db()

app = Flask(__name__)

EMAIL_PATTERN = re.compile(r"^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$")

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/stocks")
def stocks_prices_display():
    try:
        prices = get_prices_open()
        market_open = check_exchange_open()
        return render_template("stocks.html", prices=prices, market_open=market_open, active="stocks")
    except Exception as e:
        return render_template("error.html", message=str(e), active="stocks")

@app.route("/how-it-works")
def how_it_works():
    return render_template("how-it-works.html", active="how")

@app.route("/features")
def features():
    return render_template("features.html", active="features")

@app.route("/tech")
def tech():
    return render_template("tech.html", active="tech")

@app.route("/get-started")
def get_started():
    return render_template("get-started.html", active="get-started")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    to_email = request.form.get("email", "").strip()

    if not EMAIL_PATTERN.match(to_email):
        return render_template(
            "get-started.html",
            active="get-started",
            error="Please enter a valid email address."
        )

    add_subscriber(to_email)
    result = send_daily_digest(to_email)

    return render_template("subscribed.html", result=result, email=to_email)

@app.errorhandler(500)
def handle_500(e):
    return render_template("error.html", message="Something unexpected happened on our end."), 500

if __name__ == "__main__":
    app.run(debug=True)