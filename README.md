
# MarketInsightTool

**A Python + Flask Web App to Analyze Financial Instruments**

MarketInsightTool is a lightweight, interactive financial analytics dashboard that provides real-time stock performance analysis using public data from Yahoo Finance. It is designed for job seekers, analysts, and investors who want fast insights into market behavior with professional-quality metrics and charts.
---

## Features

- Input any stock ticker (e.g., AAPL, TCS.NS, MSFT)
- Fetches real-time data via Yahoo Finance (yfinance)
- Computes advanced metrics:
  - Total Return (%)
  - Average Daily Return (%)
  - Volatility (%)
  - Sharpe Ratio
  - Maximum Drawdown
  - Relative Strength Index (RSI) using Wilder’s Method
- Interactive Plotly charts rendered in the browser
- Clean and responsive UI using Flask + Bootstrap
- Deployed on Render (cloud-hosted, ready to access)

---

## Sample Tickers to Try

- `AAPL` – Apple Inc.
- `TCS.NS` – Tata Consultancy Services (NSE)
- `MSFT` – Microsoft Corporation
- `GOOG` – Alphabet Inc.
- `INFY.NS` – Infosys Limited (NSE)

---


## Tech Stack

- Python 3.11+
- Flask – Web backend
- Plotly – Interactive chart rendering
- pandas, numpy, matplotlib – Data analysis
- yfinance – Real-time financial data
- Bootstrap CSS – Responsive frontend design
- Deployed on Render

---

## How to Run Locally

# 1. Clone the repository
git clone https://github.com/paras1234-eng/MarketInsightTool.git
cd MarketInsightTool

# 2. Create a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
```

Then open `https://marketinsighttool.onrender.com/` in your browser.

---

## Accessing Deployed Version

**Live Demo (Hosted on Render)**:  
*Actual URL*    https://dashboard.render.com/  

If access is restricted, please email me for access or use the credentials provided in my CV.

---

## Project Structure

```
MarketInsightTool/
│
├── app.py                # Flask entry point
├── fetch_data.py         # Yahoo Finance data fetcher
├── analyze_returns.py    # Financial analytics & indicators
├── plotly_chart.py       # Plotly chart generator
├── requirements.txt      # Python dependencies
├── Procfile              # Render deployment config
├── AAPL_data.csv         # Sample static dataset
├── .gitignore            # Ignore generated files
├── templates/
│   └── index.html        # Web page template
```

---

## License

This project is for educational and demonstration purposes only. Not intended for actual trading or investment advice. Please do not reproduce or distribute without permission.

---

## Author

**Paras**  
Business Analyst | Aspiring Python Developer  
Email: *Available in CV*  
Location: UK

---

*If you like this project, feel free to share feedback or reach out for collaborations.*
