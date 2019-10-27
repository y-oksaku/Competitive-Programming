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
    items = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [float('inf')] * (10**5 + 1)
    dp[0] = 0

    for w, v in items:
        for value in range(10**5 + 1)[:: -1]:
            if value - v >= 0:
                dp[value] = min(dp[value], dp[value - v] + w)

    ans = 0
    for v in range(10**5 + 1)[:: -1]:
        if dp[v] <= W:
            ans = v
            break

    print(ans)


sol()