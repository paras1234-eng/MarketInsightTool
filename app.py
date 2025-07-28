from plotly_chart import generate_price_chart


from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def create_plot(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Close"], label="Close Price")
    plt.plot(df["MA20"], label="20-Day MA")
    plt.plot(df["MA50"], label="50-Day MA")
    plt.legend()
    plt.title("Stock Price & Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route("/", methods=["GET", "POST"])
def index():
    plot_url = None
    summary = None
    ticker = ""

    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        data = yf.download(ticker, period="1y", group_by="ticker", auto_adjust=False)
        print("Downloaded columns:", data.columns)

        # ✅ Fix: Flatten MultiIndex by selecting correct level
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(1)

        data.reset_index(inplace=True)
        data["Date"] = pd.to_datetime(data["Date"])
        data.set_index("Date", inplace=True)

        expected_cols = ["Open", "High", "Low", "Close", "Volume"]
        for col in expected_cols:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col], errors="coerce")
            else:
                print(f"⚠️ Missing column: {col}")
                return render_template("index.html", summary=None, plot_url=None, ticker=ticker)

        # Calculations
        data["Daily Return"] = data["Close"].pct_change()
        data["Cumulative Return"] = (1 + data["Daily Return"]).cumprod()
        data["MA20"] = data["Close"].rolling(window=20).mean()
        data["MA50"] = data["Close"].rolling(window=50).mean()
        data["Volatility"] = data["Daily Return"].rolling(window=20).std()

        # Drawdown
        rolling_max = data["Cumulative Return"].cummax()
        drawdown = data["Cumulative Return"] / rolling_max - 1
        max_drawdown = drawdown.min()

                # Extra insights
        avg_daily_return = data["Daily Return"].mean()
        sharpe_ratio = (avg_daily_return / data["Volatility"].mean()) * (252**0.5)
        delta = data["Close"].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        latest_rsi = round(rsi.iloc[-1], 2)

        # Summary
        summary = {
            "Ticker": ticker,
            "Start Date": data.index.min().strftime("%Y-%m-%d"),
            "End Date": data.index.max().strftime("%Y-%m-%d"),
            "Total Return (%)": round((data["Cumulative Return"].iloc[-1] - 1) * 100, 2),
            "Avg Daily Return (%)": round(avg_daily_return * 100, 2),
            "Volatility (%)": round(data["Volatility"].mean() * 100, 2),
            "Max Drawdown (%)": round(max_drawdown * 100, 2),
            "Sharpe Ratio": round(sharpe_ratio, 2),
            "RSI": latest_rsi
        }


        plot_url = generate_price_chart(data)


    return render_template("index.html", summary=summary, plot_url=plot_url, ticker=ticker)

if __name__ == "__main__":
    app.run(debug=True)


