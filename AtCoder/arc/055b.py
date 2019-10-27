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
    N, K = map(int, input().split())

    dp = [[[0, 0] for _ in range(K + 2)] for _ in  range(N + 1)]

    for k in range(K + 1):
        dp[N][k][1] = 1.0

    for n in range(N)[:: -1]:
        for k in range(K + 1):
            if k > n:
                break
            for i in range(2):
                dp[n][k][i] = n / (n + 1) * dp[n + 1][k][i] + max(dp[n + 1][k + 1][1], dp[n + 1][k][0]) / (n + 1)

    print(dp[0][0][0])

sol()