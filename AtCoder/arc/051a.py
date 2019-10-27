import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def dist(x, y, u, v):
    return ((x - u)**2 + (y - v)**2)**0.5

def sol():
    CX, CY, r = map(int, input().split())

    L, D, R, U = map(int, input().split())

    if L <= CX - r and R >= CX + r and D <= CY - r and U >= CY + r:
        print('NO')
    else:
        print('YES')

    if all([dist(CX, CY, x, y) <= r for x, y in [(L, U), (L, D), (R, U), (R, D)]]):
        print('NO')
    else:
        print('YES')


sol()