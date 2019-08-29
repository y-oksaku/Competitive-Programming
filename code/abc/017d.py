import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N, _ = map(int, input().split())

    A = [0] * N
    for i in range(N):
        A[i] = int(input())

    V = set()
    dp = [0] * (N + 2)
    ims = [0] * (N + 2)
    ims[0] = 1
    ims[1] = -1
    right = 0
    add = 0

    for left in range(N):
        while right < N and not A[right] in V:
            V.add(A[right])
            right += 1

        add = (add + ims[left]) % MOD
        dp[left] = add
        ims[left + 1] += dp[left]
        ims[right + 1] -= dp[left]
        V.remove(A[left])

    for i in range(N):
        ims[i + 1] = (ims[i + 1] + ims[i]) % MOD

    print(ims[N])

sol()