import json
from multiprocessing import Pool
import time

import pandas as pd


with open("secrets.json", 'r') as fr:
    content = "".join(fr.readlines())
    API_KEY = json.loads(content)['eod_histo_data_api_key']

TICKERS = ["NVDA.US", "TSLA.US", "MSFT.US", "AMZN.US", "NFLX.US", "TWTR.US",
           "PYPL.US", "ADBE.US", "V.US", "ASML.US", "AMD.US", "META.US",
           "INTC.US", "MA.US", "AAPL.US", "GOOGL.US", "BTC-USD.CC",
           "ETH-USD.CC", "BNB-USD.CC", "DOGE-USD.CC"]
FROM = "2020-01-01"
TO = "2022-01-01"


def worker(ticker):
    url = f"https://eodhistoricaldata.com/api/eod/{ticker}?api_token={API_KEY}&from={FROM}&to={TO}"
    df = pd.read_csv(url, skipfooter=1, engine='python')
    df['Symbol'] = ticker
    print(ticker)
    return df


if __name__ == '__main__':
    df = pd.DataFrame()
    start = time.perf_counter()
    with Pool() as p:
        for quotes in p.map(worker, TICKERS):
            df = pd.concat([df, quotes], ignore_index=True)
    elapsed_time = time.perf_counter() - start
    print(f"{len(TICKERS)} contracts in {elapsed_time:0.2f} seconds")
    print(len(df))
