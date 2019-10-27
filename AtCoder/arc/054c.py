import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')
EPS = 1e-8

import math


def sol():
    P = float(input())

    left = 0
    right = P

    def f(x):
        return x + P * pow(2, -x / 1.5)

    def isOk(x):
        if f(x) <= f(x + EPS):
            return True
        else:
            return False

    while abs(right - left) > EPS:
        mid = (left + right) / 2
        if isOk(mid):
            right = mid
        else:
            left = mid

    print(f(left))

sol()