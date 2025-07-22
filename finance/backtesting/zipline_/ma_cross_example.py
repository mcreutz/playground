import os

import yfinance as yf
import pandas as pd

from zipline import run_algorithm
from zipline.api import (
    order_target_percent,
    symbol,
    schedule_function,
    date_rules,
    time_rules,
)
from zipline.data.bundles import ingest, register
from zipline.data.bundles.csvdir import csvdir_equities


STOCKS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "JNJ", "V"]

# Download data and save as CSV files
print("Downloading data...")
data = yf.download(STOCKS, start="2021-12-01", end="2024-12-31", progress=False)
os.makedirs("yfinance_data", exist_ok=True)

for stock in STOCKS:
    df = pd.DataFrame(
        {
            "open": data[("Open", stock)],
            "high": data[("High", stock)],
            "low": data[("Low", stock)],
            "close": data[("Close", stock)],
            "volume": data[("Volume", stock)],
        }
    ).dropna()
    df.index.name = "date"
    df.to_csv(f"yfinance_data/{stock}.csv")

# Register the yfinance bundle
os.environ["CSVDIR"] = os.path.abspath("yfinance_data")
register(
    "yfinance",
    csvdir_equities([os.path.abspath("yfinance_data")]),
    calendar_name="NYSE",
)


def initialize(context):
    context.stocks = [symbol(stock) for stock in STOCKS]
    schedule_function(rebalance, date_rules.week_start(), time_rules.market_open())


def rebalance(context, data):
    ma_diffs = {}
    for stock in context.stocks:
        try:
            prices = data.history(stock, "price", 40, "1d")
            if len(prices) >= 30:
                fast_ma = prices.rolling(10).mean().iloc[-1]
                slow_ma = prices.rolling(30).mean().iloc[-1]
                ma_diffs[stock] = fast_ma - slow_ma
        except:
            continue

    if ma_diffs:
        sorted_stocks = sorted(ma_diffs.items(), key=lambda x: x[1], reverse=True)
        top_stocks = [stock for stock, _ in sorted_stocks[:3]]

        for stock in context.stocks:
            weight = 1 / 3 if stock in top_stocks else 0
            order_target_percent(stock, weight)


def analyze(context, perf):
    total_return = (
        perf["portfolio_value"].iloc[-1] / perf["portfolio_value"].iloc[0] - 1
    ) * 100
    print(f"Total Return: {total_return:.1f}%")


# Ingest the yfinance bundle and run
ingest("yfinance")
print("Running backtest...")
result = run_algorithm(
    start=pd.Timestamp("2022-01-01"),
    end=pd.Timestamp("2024-12-31"),
    initialize=initialize,
    analyze=analyze,
    capital_base=100000,
    data_frequency="daily",
    bundle="yfinance",
)
