import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    S = input().strip()
    T = input().strip()

    lenS = len(S)
    lenT = len(T)

    dp = [[0] * (lenT + 1) for _ in range(lenS + 1)]

    for i, s in enumerate(S):
        for j, t in enumerate(T):
            if s == t:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    ans = []
    now = dp[lenS][lenT]
    i = lenS
    j = lenT
    while now > 0:
        if dp[i - 1][j] == now:
            i -= 1
        elif dp[i][j - 1] == now:
            j -= 1
        else:
            ans.append(S[i - 1])
            i -= 1
            j -= 1
            now -= 1

    print(''.join(ans[:: -1]))

sol()