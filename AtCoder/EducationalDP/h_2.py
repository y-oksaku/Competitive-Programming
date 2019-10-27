import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    H, W = map(int, input().split())
    chart = [[False] * (W + 2) for _ in range(H + 2)]

    for h in range(1, H + 1):
        line = input()
        for w, s in enumerate(line):
            if s == '.':
                chart[h][w + 1] = True

    dp = [[0] * (W + 2) for _ in range(H + 2)]
    dp[1][1] = 1

    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if chart[h + 1][w]:
                dp[h + 1][w] = (dp[h + 1][w] + dp[h][w]) % MOD
            if chart[h][w + 1]:
                dp[h][w + 1] = (dp[h][w + 1] + dp[h][w]) % MOD

    print(dp[H][W] % MOD)

sol()