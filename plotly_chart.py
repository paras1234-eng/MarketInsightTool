import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from markupsafe import Markup


def generate_price_chart(df):
    df['20_MA'] = df['Close'].rolling(window=20).mean()
    df['50_MA'] = df['Close'].rolling(window=50).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index, y=df['Close'],
        mode='lines', name='Close Price',
        line=dict(color='blue')
    ))

    fig.add_trace(go.Scatter(
        x=df.index, y=df['20_MA'],
        mode='lines', name='20-Day MA',
        line=dict(color='orange')
    ))

    fig.add_trace(go.Scatter(
        x=df.index, y=df['50_MA'],
        mode='lines', name='50-Day MA',
        line=dict(color='green')
    ))

    fig.update_layout(
        title='Price Chart with Moving Averages',
        xaxis_title='Date',
        yaxis_title='Price',
        legend_title='Legend',
        height=500
    )

    # Convert Plotly figure to embeddable HTML
    chart_html = pio.to_html(fig, full_html=False)
    return Markup(chart_html)
