import math
import random
import time

t0 = time.time()
for i in range(int(1e7)):
    math.sin(math.cos(random.random()))

print(time.time() - t0)
