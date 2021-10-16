import ib_insync
from time import sleep

ib = ib_insync.ib.IB()
ib.RaiseRequestErrors = True

ib.connect(
    host="127.0.0.1",
    port=7497,
    clientId=1,
    readonly=True)

ib_contract = ib_insync.contract.Stock(
    symbol="DAI",
    exchange="IBIS",
    currency="EUR")

try:
    bar_data = ib.reqHistoricalData(
        contract=ib_contract,
        endDateTime='',
        durationStr="30 D",
        barSizeSetting='1 day',
        whatToShow='ADJUSTED_LAST',
        useRTH=True)
except ib_insync.wrapper.RequestError as e:
    print(e)
else:
    print(bar_data)
