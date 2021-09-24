import multiprocessing
import pandas as pd

# multiprocessing.set_start_method('fork', True)

class MyClass():

    def __init__(self):
        pass

    def f(self, x):
        return pd.DataFrame()

    def multi_f(self, ):
        with multiprocessing.Pool(2) as p:
            print(p.map(self.f, [1, 2, 3]))

