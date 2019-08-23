import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())
    prob = map(float, input().split())

    dp = [0] * (N + 1)  # dp[head]
    dp[0] = 1

    for p in prob:
        for count in range(1, N + 1)[:: -1]:
            dp[count] = dp[count] * (1 - p) + dp[count - 1] * p
        dp[0] *= (1 - p)

    print(sum(dp[(N + 1) // 2:]))


sol()