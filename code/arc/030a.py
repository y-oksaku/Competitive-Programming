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
    K = int(input())

    if K == 1:
        print('YES')
        return

    if N >= 2 * K:
        print('YES')
    else:
        print('NO')


sol()