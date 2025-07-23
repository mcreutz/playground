import os
import warnings

import yfinance as yf
import pandas as pd

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore", category=FutureWarning)

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
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"


def download_data():
    """Download yfinance data and save as CSV files"""
    print("Downloading data...")
    data = yf.download(
        STOCKS, start=START_DATE, end=END_DATE, progress=False, auto_adjust=True
    )
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


def setup_bundle():
    """Register and ingest the yfinance bundle"""
    os.environ["CSVDIR"] = os.path.abspath("yfinance_data")
    register(
        "yfinance",
        csvdir_equities([os.path.abspath("yfinance_data")]),
        calendar_name="NYSE",
    )
    ingest("yfinance")


def rebalance(context, data):
    """Weekly rebalancing function"""
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


def initialize(context):
    """Initialize the zipline algorithm"""
    context.stocks = [symbol(stock) for stock in STOCKS]
    schedule_function(rebalance, date_rules.week_start(), time_rules.market_open())


def analyze(context, perf):
    """Analyze performance results"""
    initial_value = perf["portfolio_value"].iloc[0]
    final_value = perf["portfolio_value"].iloc[-1]

    # Calculate total return
    total_return = ((final_value / initial_value) - 1) * 100

    # Calculate annualized return
    start_date = pd.to_datetime(START_DATE)
    end_date = pd.to_datetime(END_DATE)
    years = (end_date - start_date).days / 365.25
    annualized_return = ((final_value / initial_value) ** (1 / years) - 1) * 100

    print(f"Total Return: {total_return:.1f}%")
    print(f"Annualized Return: {annualized_return:.1f}%")
    print(f"Years: {years:.1f}")


def run_backtest():
    print("Running backtest...")
    run_algorithm(
        start=pd.Timestamp(START_DATE),
        end=pd.Timestamp(END_DATE),
        initialize=initialize,
        analyze=analyze,
        capital_base=100000,
        data_frequency="daily",
        bundle="yfinance",
    )


def main():
    """Run the complete backtest"""
    download_data()
    setup_bundle()
    run_backtest()


if __name__ == "__main__":
    main()
