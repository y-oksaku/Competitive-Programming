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
    A = list(map(int, input().split()))

    twoCount = 0
    oneCount = 0
    for a in A:
        if a == 2:
            twoCount += 1
        if a == 1:
            oneCount += 1
    threeCount = N - oneCount - twoCount

    dp = [[[0] * (threeCount + 2) for _ in range(twoCount + 2)] for _ in range(oneCount + 2)]
    dp2 = [[[0] * (threeCount + 2) for _ in range(twoCount + 2)] for _ in range(oneCount + 2)]
    dp[oneCount][twoCount][threeCount] = 1

    ans = 0
    for time in range(1, 1000):
        for one in range(oneCount + 1):
            for two in range(twoCount + 1):
                for three in range(threeCount + 1):
                    if one > 0:
                        dp2[one - 1][two][three] += dp[one][two][three] * (one / N)
                    if two > 0:
                        dp2[one + 1][two - 1][three] += dp[one][two][three] * (two / N)
                    if three > 0:
                        dp2[one][two + 1][three - 1] += dp[one][two][three] * (three / N)
        print(dp)
        ans += dp2[0][0][0] * time
        dp[oneCount][twoCount][threeCount] = 0
        dp2[oneCount][twoCount][threeCount] = 0
        dp2, dp = dp, dp2

    print(ans)

sol()