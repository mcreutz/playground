# Finding the differences in 2 lists

import datetime
import random

length = 20000
l1 = []
l2 = []

for _ in range(length):
    l1.append(random.random())
    l2.append(random.random())


# Using lists, this is slow !!
start = datetime.datetime.now()
d1 = []
for element in l1:
    if element not in l2:
        d1.append(element)
d2 = []
for element in l2:
    if element in l1:
        d2.append(element)
duration = datetime.datetime.now() - start
print(duration)


# Using sets, much faster (~600x) !!
start = datetime.datetime.now()
s1 = set(l1)
s2 = set(l2)
dd1 = s1.difference(s2)
dd2 = s2.difference(s1)
duration = datetime.datetime.now() - start
print(duration)
