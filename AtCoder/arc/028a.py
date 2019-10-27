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
    N, A, B = map(int, input().split())

    while N > 0:
        N -= A
        if N <= 0:
            print('Ant')
            return
        N -= B
        if N <= 0:
            print('Bug')
            return

sol()