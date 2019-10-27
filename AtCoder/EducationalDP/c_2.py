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
    actions = []


    for _ in range(N):
        a, b, c = map(int, input().split())
        actions.append((a, b, c))

    dp = [[0] * 3 for _ in range(N + 1)]  # dp[day][prevAct]

    for day, (a, b, c) in enumerate(actions):
        dp[day + 1][0] = max(dp[day][1], dp[day][2]) + a
        dp[day + 1][1] = max(dp[day][2], dp[day][0]) + b
        dp[day + 1][2] = max(dp[day][0], dp[day][1]) + c

    ans = max(dp[N])
    print(ans)


sol()