import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, A, B, C, D = map(int, input().split())

    A, B = min(A, B), max(A, B)
    diff = B - A

    for plus in range(N):
        if C * (N - 1 - plus) - D * plus <= diff<= -C * plus + D * (N - 1 - plus):
            print('YES')
            return

    print('NO')

sol()