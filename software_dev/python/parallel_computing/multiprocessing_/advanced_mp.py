import multiprocessing
import pandas as pd


def f(x):
    return pd.DataFrame()


def multi_f():
    with multiprocessing.Pool(2) as p:
        print(p.map(self.f, [1, 2, 3]))


def square(x):
    return x * x


# link results to initial parameters
def multi_square():
    my_nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }
    my_squares = {}
    with multiprocessing.Pool() as p:
        result = p.map(square, my_nums.values())
    for i, key in enumerate(my_nums.keys()):
        my_squares[key] = result[i]
    print(my_squares)


if __name__ == "__main__":
    multi_square()


# use imap() for large data. is lazier than map().
# also use chunksize param to control how many tasks are sent to each process at a time.
