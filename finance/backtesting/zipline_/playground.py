from zipline.api import order, record, symbol
from zipline import run_algorithm
from zipline.utils.cli import Date


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))


if __name__ == '__main__':
    start = Date(tz='utc', as_timestamp=True).parser('2017-10-15')
    end = Date(tz='utc', as_timestamp=True).parser('2017-11-01')
    
    run_algorithm(start, end, initialize, 10e6, handle_data=handle_data)

