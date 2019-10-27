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
    H = list(map(int, input().split())) + [float('inf'), float('inf')]

    minCost = [float('inf')] * (N + 2)
    minCost[0] = 0

    for i in range(N):
        minCost[i + 1] = min(minCost[i + 1], minCost[i] + abs(H[i] - H[i + 1]))
        minCost[i + 2] = min(minCost[i + 2], minCost[i] + abs(H[i] - H[i + 2]))

    print(minCost[N - 1])


sol()