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
    scores = [int(input()) for _ in range(N)]

    scores.sort()

    if scores[-1] < scores[0] * 8:
        print(0)
        return

    upper = [-1 for _ in range(N)]
    for i, s in enumerate(scores):
        upper[i] = bisect_left(scores, 2 * s)

    dp = [1] * N
    for _ in range(3):
        dp2 = [0] * N
        for i, n in enumerate(dp):
            to = upper[i]
            if to == N:
                break
            dp2[to] += n
        for i in range(N - 1):
            dp2[i + 1] = (dp2[i + 1] + dp2[i]) % MOD
        dp = dp2

    print(sum(dp) % MOD)

sol()