import sys
import math
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')
EPS = 1e-8

A, B, C = map(int, input().split())

def func(t):
    return A * t + B * math.sin(math.pi * C * t) - 100

for mul in range(1, 10000):
    maxT = 1 / (2 * C) + (2 / C) * mul
    if func(maxT) > 0:
        minT = 0
        while abs(func(minT)) > EPS:
            mid = (minT + maxT) / 2
            if func(mid) > 0:
                maxT = mid
            else:
                minT = mid

        print(minT)
        break