from datetime import date
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from data import get_prices_open

load_dotenv()


def check_exchange_open():
    """Returns True if today is a weekday (Mon-Fri), False on weekends."""
    today = date.today().weekday()      # Monday: 0, Sunday: 6
    return today in range(5)


def build_email_body():
    prices_open = get_prices_open()
    today_str = date.today().strftime("%B %d, %Y")

    price_lines = "\n".join(
        [f"{symbol:<7}→  ${price}" for symbol, price in prices_open.items()]
    )

    return f"""Good morning, investor! ☀️

Here's your daily stock snapshot for today, {today_str}.

📊 Today's Prices:

{price_lines}

That's the wrap for today. Catch you tomorrow at 9:30.
"""


def send_daily_digest(to_email):
    # """
    # Sends the stock digest to to_email.
    # Returns a dict: {"success": bool, "message": str}
    # """
    # if not check_exchange_open():
    #     return {"success": False, "message": "The stock exchange is closed today. No digest was sent."}

    my_email = os.getenv("my_email")
    port_password = os.getenv("port_password")
    email_body = build_email_body()

    msg = MIMEText(email_body, "plain", "utf-8")
    msg["Subject"] = "📈 The 9:35AM Stock Digest"
    msg["From"] = my_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=port_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=msg.as_string()
            )
        return {"success": True, "message": f"Digest sent to {to_email}!"}

    except Exception as e:
        return {"success": False, "message": f"Something went wrong: {e}"}


if __name__ == "__main__":
    test_email = input("Enter your gmail: ")
    result = send_daily_digest(test_email)
    print(result["message"])