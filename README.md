# Stock Digest 📈

A lightweight, visually striking stock market newsletter application built with Python and Flask. Stock Digest (frontend: *Stock Alert*) tracks live market data for top-performing US equities and delivers an email digest directly to subscribers via SMTP. 

Built strictly as a zero-cost personal project, this repository serves as an exercise in iterative frontend design, lightweight backend architecture, and platform-specific deployment.

## 🔄 The Journey & Technical Pivots

This project went through several architectural and design pivots to balance aesthetics with a strict ₹0 budget and simplified maintenance:

* **Frontend Evolution:** The user interface went through massive iterations. It started with a single static button, evolved into floating cards, shifted to structured grids, experimented with a marquee ticker, and finally settled on a full-viewport, fixed cascading background featuring infinite-scrolling glassmorphism stock cards natively rendered via Jinja2 loops.
* **Database & Hosting Pivot:** Initial deployment plans involved modern cloud hosts (like Render or Heroku). However, their ephemeral filesystems would have required migrating the simple SQLite database to a heavier cloud PostgreSQL/MySQL instance. To keep the project lightweight and maintain the local `subscribers.db` file, the architecture was pivoted to **PythonAnywhere**, which provides a persistent digital filesystem for free.
* **Automation Pivot:** The original goal was to automate the email dispatch strictly at 9:35 AM IST. After exploring GitHub Actions, Render Cron Jobs, and hitting the paywall for PythonAnywhere's Scheduled Tasks, the project deliberately pivoted away from complex webhooks (like external cron-job.org pingers). The dispatch is now handled by manually executing the standalone `send_digest.py` script, keeping the architecture purely decoupled and maintenance-free.

## 🛠️ Tech Stack

* **Backend:** Python 3.10, Flask
* **Database:** SQLite3 (`db.py` handles schemas and subscriber logic)
* **APIs:** Twelve Data API (Live market data fetching)
* **Email:** Standard Python `smtplib` / `email.mime`
* **Frontend:** HTML5, CSS3 (Custom Glassmorphism), Jinja2
* **Deployment Environment:** PythonAnywhere (Manual WSGI configuration)

## 📂 Project Structure

```text
stock-digest/
├── app.py                 # Main Flask application and web routing
├── db.py                  # SQLite database logic (inserts/deletes/queries)
├── send_digest.py         # Standalone script to compile data and fire SMTP emails
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys, SMTP credentials)
└── templates/             # Jinja2 HTML templates
    ├── base.html          # Core layout and CSS links
    ├── index.html         # Hero canvas and cascading stock UI
    ├── features.html      
    ├── get-started.html   
    ├── how-it-works.html  
    ├── stocks.html        
    ├── subscribed.html    
    └── tech.html          
```

## ⚙️ Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NAV-ON-WINDOWS/stock-digest.git
   cd stock-digest
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # source venv/bin/activate    # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your secure credentials. Ensure this file remains ignored by Git.
   ```env
   TWELVE_DATA_API_KEY=your_api_key_here
   SMTP_EMAIL=your_sender_email@gmail.com
   SMTP_PASSWORD=your_app_password
   ```

5. **Run the web application:**
   ```bash
   python -m flask run
   ```
   The frontend will be live at `http://127.0.0.1:5000`.

## ☁️ Deployment (PythonAnywhere)

The application is hosted on PythonAnywhere to leverage its persistent storage for the SQLite database.

1. **Server Setup:** Clone the repository directly via the PythonAnywhere Bash console and establish the virtual environment explicitly using Python 3.10:
   ```bash
   git clone https://github.com/NAV-ON-WINDOWS/stock-digest.git
   cd stock-digest
   mkvirtualenv --python=python3.10 venv
   pip install -r requirements.txt
   nano .env # Paste credentials here
   ```

2. **WSGI Configuration:** On the PythonAnywhere **Web** tab, select **Manual Configuration** (Python 3.10). Link the virtualenv path (`/home/StockDigest/.virtualenvs/venv`) and update the WSGI file to load the `.env` variables and serve the Flask app:
   ```python
   import sys
   import os
   from dotenv import load_dotenv

   project_home = '/home/StockDigest/stock-digest'
   if project_home not in sys.path:
       sys.path = [project_home] + sys.path

   load_dotenv(os.path.join(project_home, '.env'))

   from app import app as application
   ```

3. **Static Routing:** CSS and assets are routed directly via the Web tab's Static Files section (`URL: /static/`, `Directory: /home/StockDigest/stock-digest/static`) for faster rendering.

## 🚀 Sending the Digest

Because scheduled tasks are bypassed, the email engine is entirely decoupled from the Flask web server. To dispatch the daily emails, simply run the isolated script from the terminal or the PythonAnywhere Bash console:

```bash
python send_digest.py
```
This script will query the SQLite database for all registered subscribers, fetch the latest market payload from Twelve Data, and execute the SMTP dispatch loop.

---
**Author:** Arnav Salgarkar  
**GitHub:** [@NAV-ON-WINDOWS](https://github.com/NAV-ON-WINDOWS)