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
    N, B1, B2, B3 = map(int, input().split())

    L = [list(map(int, input().split())) for _ in range(N)]
    R = [list(map(int, input().split())) for _ in range(N)]

    for l in L:
        print(*l)

sol()