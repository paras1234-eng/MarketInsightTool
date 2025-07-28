# 📊 MarketInsightTool

### A Python + Flask Web App to Analyze Financial Instruments

**MarketInsightTool** is a lightweight, interactive financial analytics dashboard that provides real-time stock performance analysis using public data from Yahoo Finance. It is designed for job seekers, analysts, and investors who want fast insights into market behavior with professional-quality metrics and charts.

---

## 🚀 Features

- Input **any stock ticker** (e.g., `AAPL`, `TCS.NS`, `MSFT`)
- Fetches **real-time data** via Yahoo Finance (`yfinance`)
- Computes key financial metrics:
  - Total Return (%)
  - Average Daily Return (%)
  - Volatility (%)
  - **Sharpe Ratio**
  - **Relative Strength Index (RSI)** using Wilder’s Method
  - Maximum Drawdown
- **Interactive Plotly charts** rendered in the browser
- Clean and responsive UI using Flask + Bootstrap
- **Deployed on Render** (cloud-hosted and public)

---

## 🔍 Sample Tickers to Try

| Ticker     | Company Name                        |
|------------|-------------------------------------|
| `AAPL`     | Apple Inc.                          |
| `TCS.NS`   | Tata Consultancy Services (India)   |
| `MSFT`     | Microsoft Corporation               |
| `GOOG`     | Alphabet Inc.                       |
| `INFY.NS`  | Infosys Limited (India)             |

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Flask** – Web backend
- **Plotly** – Interactive chart rendering
- **pandas**, **numpy**, **matplotlib** – Data analysis
- **yfinance** – Real-time financial data
- **Bootstrap CSS** – Responsive frontend design
- **Deployed on Render**

---

## 💻 How to Run Locally

```bash
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

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🌐 Accessing Deployed Version

**Live Demo**:  
🔗 [https://marketinsighttool.onrender.com](https://marketinsighttool.onrender.com)

If access is restricted, please contact me or refer to credentials in my CV.

---

## 📁 Project Structure

```
MarketInsightTool/
├── app.py                # Flask entry point
├── fetch_data.py         # Yahoo Finance data fetcher
├── analyze_returns.py    # Financial analytics & indicators
├── plotly_chart.py       # Plotly chart generator
├── requirements.txt      # Python dependencies
├── Procfile              # Render deployment config
├── AAPL_data.csv         # Sample static dataset
├── .gitignore            # Ignore generated files like summary reports
└── templates/
    └── index.html        # Web page template
```

---

## ⚠️ License

This project is for **educational and demonstration purposes only**. Not intended for trading or investment advice. Please do not reproduce or distribute without permission.

---

## 👤 Author

**Paras**  
Business Analyst | Aspiring Python Developer  
📍 UK | 📧 Contact available in CV

---

*If you like this project, feel free to share feedback or reach out for collaborations.*