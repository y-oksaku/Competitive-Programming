import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, P = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    items.sort(key=itemgetter(0), reverse=True)

    dp = [0] * (P + 1)
    ans = 0

    for price, value in items:
        for p in range(P + 1)[:: -1]:
            ans = max(ans, dp[p] + value)
            if p - price >= 0:
                dp[p] = max(dp[p], dp[p - price] + value)

    print(ans)

sol()