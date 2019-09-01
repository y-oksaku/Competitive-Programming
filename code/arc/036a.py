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

    T = []
    for _ in range(N):
        t = int(input())
        T.append(t)
    T.append(0)

    now = sum(T[: 3])
    ans = -1
    for day in range(3, N + 1):
        if now < K:
            ans = day
            break
        now += T[day]
        now -= T[day - 3]

    print(ans)

sol()