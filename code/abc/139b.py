import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    A, B = map(int, input().split())

    if B == 1:
        print(0)
        return

    now = 1
    for i in range(1, 1000):
        now += A - 1
        if now >= B:
            print(i)
            return


sol()