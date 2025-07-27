import pandas as pd
import numpy as np

def analyze_returns(data):
    # Convert 'Date' column to datetime and set as index
    data["Date"] = pd.to_datetime(data["Date"])
    data.set_index("Date", inplace=True)

    # Convert numeric columns from string to float
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # Calculate daily returns
    data["Daily Return"] = data["Close"].pct_change()

    # Calculate cumulative returns
    data["Cumulative Return"] = (1 + data["Daily Return"]).cumprod()

    # Calculate volatility (rolling std dev of daily returns)
    data["Volatility"] = data["Daily Return"].rolling(window=14).std()

    # Max drawdown
    cumulative_max = data["Cumulative Return"].cummax()
    drawdown = (data["Cumulative Return"] - cumulative_max) / cumulative_max
    data["Max Drawdown"] = drawdown

    # Sharpe Ratio
    mean_daily_return = data["Daily Return"].mean()
    std_daily_return = data["Daily Return"].std()
    sharpe_ratio = (mean_daily_return / std_daily_return) * np.sqrt(252)

    # Compute RSI using Wilder's method
    def compute_rsi_wilder(data, window=14):
        delta = data["Close"].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()
        avg_loss = loss.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    data["RSI"] = compute_rsi_wilder(data)

    # Final summary metrics
    total_return = (data["Cumulative Return"].iloc[-1] - 1) * 100
    avg_daily_return = data["Daily Return"].mean() * 100
    volatility = data["Daily Return"].std() * 100
    max_drawdown = drawdown.min() * 100
    rsi_latest = data["RSI"].iloc[-1]

    summary = {
        "Start Date": data.index.min().date(),
        "End Date": data.index.max().date(),
        "Total Return (%)": round(total_return, 2),
        "Average Daily Return (%)": round(avg_daily_return, 2),
        "Volatility (%)": round(volatility, 2),
        "Max Drawdown (%)": round(max_drawdown, 2),
        "Sharpe Ratio": round(sharpe_ratio, 2),
        "RSI": round(rsi_latest, 2)
    }

    return data, summary

