
# MarketInsightTool

**A Python + Flask Web App to Analyze Financial Instruments**

MarketInsightTool is a lightweight financial analytics dashboard designed to provide real-time stock analysis using public data. It offers core investment metrics such as total return, average daily return, volatility, Sharpe Ratio, RSI, and maximum drawdown for any stock ticker available on Yahoo Finance.

---

## Features

- Input any stock ticker (e.g., AAPL, TCS.NS, MSFT)
- Real-time data fetched from Yahoo Finance
- Computes advanced metrics:
  - Total Return (%)
  - Average Daily Return (%)
  - Volatility (%)
  - Sharpe Ratio
  - Maximum Drawdown
  - RSI (Wilder’s Method)
- Clean and responsive web UI (Flask + HTML + Bootstrap)
- Hosted on Render (free-tier deployment)

---

## Sample Tickers to Try

- `AAPL` – Apple Inc.
- `TCS.NS` – Tata Consultancy Services (NSE)
- `MSFT` – Microsoft Corporation
- `GOOG` – Alphabet Inc.
- `INFY.NS` – Infosys Limited (NSE)

---

## Screenshots

*You can add screenshots here by uploading images named `screenshot1.png`, etc.*

---

## Tech Stack

- Python 3.11+
- Flask (Web Framework)
- yFinance (Data Source)
- pandas, numpy, matplotlib
- HTML (Jinja2 templates)
- Bootstrap CSS
- Hosted on: Render

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/paras1234-eng/MarketInsightTool.git
cd MarketInsightTool

# 2. Create virtual environment and install requirements
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## Accessing Deployed Version

**Live Demo (Hosted on Render)**:  
[https://your-render-link.onrender.com](#) *(Update with actual URL)*

If access is restricted, please email me for access or use the credentials provided in my CV.

---

## Project Structure

```
MarketInsightTool/
│
├── app.py                # Flask app runner
├── fetch_data.py         # Fetches and cleans data from yFinance
├── analyze_returns.py    # Analyzes returns, RSI, Sharpe, etc.
├── requirements.txt      # Python package dependencies
├── Procfile              # Render deployment instruction
├── AAPL_data.csv         # Sample dataset
└── templates/
    └── index.html        # Front-end web page
```

---

## License

This project is for educational and demo purposes only. Please do not reproduce or republish code without permission.

---

## Author

**Paras**  
Business Analyst | Aspiring Python Developer  
📧 Email: *Available in CV*  
🌍 Location: UK

---

*If you like this project, feel free to share feedback or reach out for collaborations.*
