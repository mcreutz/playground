#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def isprime(num):
    if num < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def primeXor(a):
    # arr = map(int, a.split(" "))
    multisets = []
    for length in range(1, len(a)+1):
        combies = combinations(a, length)
        for combie in combies:
            if combie not in multisets:
                multisets.append(combie)
    primes = 0
    for multiset in multisets:
        bwxor = 0
        for elem in multiset:
            bwxor = bwxor ^ elem
        if isprime(bwxor):
            primes += 1
    return int(primes % (10E9 + 7))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        print(str(result) + '\n')

    # fptr.close()
