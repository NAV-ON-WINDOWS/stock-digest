# Stock Digest 📈

A clean, fast, and automated stock market tracking application built with Python and Flask. Stock Digest (frontend: *Stock Alert*) fetches live market data for top-performing US equities and automatically delivers a daily email digest straight to your inbox every morning at 9:35 AM. 

The frontend features a custom-built, infinite-scrolling cascading grid of live stock cards with a modern glassmorphism aesthetic.

## 🚀 Features

* **Live Market Data:** Fetches real-time stock prices and daily percentage changes using the Twelve Data API.
* **Market-Hours Awareness:** Built-in logic ensures the application knows when markets are open, preventing stale data from being sent.
* **Automated Email Delivery:** Compiles and fires off a daily digest via SMTP automatically at 9:35 AM.
* **Dynamic Cascading UI:** A fully responsive, infinite-looping angled waterfall frontend that visualises live stock payloads seamlessly.
* **Zero Bloat:** A deliberate, lightweight stack focused purely on speed and delivery.

## 🛠️ Built With

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Jinja2 Templating
* **Data Integration:** Twelve Data API
* **Email Protocol:** SMTP

## 📂 Project Structure

```text
stock-digest/
├── app.py                 # Main Flask application and routing
├── requirements.txt       # Python dependencies
└── templates/             # Jinja2 HTML templates
    ├── base.html          # Core layout and styling
    ├── index.html         # Hero canvas and cascading stock UI
    ├── features.html      
    ├── get-started.html   
    ├── how-it-works.html  
    ├── stocks.html        
    ├── subscribed.html    
    └── tech.html          
```

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NAV-ON-WINDOWS/stock-digest.git
   cd stock-digest
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   TWELVE_DATA_API_KEY=your_api_key_here
   SMTP_EMAIL=your_sender_email@gmail.com
   SMTP_PASSWORD=your_app_password
   ```

5. **Run the application:**
   ```bash
   flask run
   ```
   The app will be live at `http://127.0.0.1:5000`.

## 👨‍💻 Author
**Arnav Salgarkar**  
GitHub: [@NAV-ON-WINDOWS](https://github.com/NAV-ON-WINDOWS)