import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, W = map(int, input().split())
    items = [0] * N

    for i in range(N):
        w, v = map(int, input().split())
        items[i] = (v, w)

    dp = [0] * (W + 1)

    for value, weight in items:
        for w in range(W + 1)[:: -1]:
            if w - weight >= 0:
                dp[w] = max(dp[w], dp[w - weight] + value)

    print(dp[W])

sol()