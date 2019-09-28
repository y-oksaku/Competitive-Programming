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
    N, M = map(int, input().split())
    keys = []

    for _ in range(M):
        a, _ = map(int ,input().split())
        C = list(map(int, input().split()))
        cMask = 0
        for c in C:
            cMask |= (1 << (c - 1))
        keys.append((a, cMask))

    dp = [[INF] * (1 << N) for _ in range(M + 1)]  # dp[i][mask] = i番目の鍵までで，状態mask
    dp[0][0] = 0

    for i, (cost, cMask) in enumerate(keys, start=1):
        for mask in range(1 << N):
            dp[i][mask] = min(dp[i][mask], dp[i - 1][mask])
            dp[i][mask | cMask] = min(dp[i][mask | cMask], dp[i - 1][mask] + cost)

    ans = dp[M][(1 << N) - 1]
    if ans == INF:
        print(-1)
    else:
        print(ans)

sol()