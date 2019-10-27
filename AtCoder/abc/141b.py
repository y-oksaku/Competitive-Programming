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
    S = input().rstrip()

    for i, s in enumerate(S):
        if i % 2 == 0:
            if s == 'L':
                print('No')
                return
        else:
            if s == 'R':
                print('No')
                return
    print('Yes')


sol()