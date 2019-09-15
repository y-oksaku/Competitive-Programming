import sys
from heapq import heappop, heappush, heapify
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    que = [-a for a in A]

    heapify(que)

    for _ in range(M):
        maxA = -heappop(que)
        heappush(que, -(maxA // 2))

    ans = -sum(que)
    print(ans)

sol()