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
    N, M = map(int, input().split())

    minDist = [[INF] * N for _ in range(N)]
    for i in range(N):
        minDist[i][i] = 0

    for _ in range(M):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        minDist[fr][to] = cost
        minDist[to][fr] = cost

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if minDist[i][j] > minDist[i][k] + minDist[k][j]:
                    minDist[i][j] = minDist[i][k] + minDist[k][j]

    minCost = INF
    for i in range(N):
        cost = max(minDist[i])
        if cost < minCost:
            minCost = cost

    print(minCost)


sol()