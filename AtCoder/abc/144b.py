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
    N = int(input())

    for i in range(1, 101):
        if N % i == 0:
            M = N // i
            if 1 <= M <= 9 and 1 <= i <= 9:
                print('Yes')
                return
    print('No')


sol()