import time
from threading import Thread


def worker():
    print('Start')
    start = time.time()

    for i in range(1, 1000*1000*10):
        n=2*i
        n=n/i

    end = time.time()
    print('Finish: ', str(end-start))


def reader():
    text = input()
    print(text)


tw = Thread(target=worker)
tr = Thread(target=reader)
tw.start()
tr.start()