from db import get_all_subscribers
from main import send_daily_digest

def send_to_all():
    subscribers = get_all_subscribers()

    if not subscribers:
        print("No subscribers yet.")
        return

    for email in subscribers:
        result = send_daily_digest(email)
        print(f"{email}: {result['message']}")


if __name__ == "__main__":
    send_to_all()