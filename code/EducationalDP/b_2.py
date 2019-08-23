import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    minCost = [float('inf')] * N
    minCost[0] = 0

    for i, h in enumerate(H):
        for k in range(1, K + 1):
            if i + k >= N:
                break
            minCost[i + k] = min(minCost[i + k], minCost[i] + abs(h - H[i + k]))

    print(minCost[N - 1])


sol()