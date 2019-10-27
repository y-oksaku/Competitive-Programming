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
    R, B = map(int, input().split())
    x, y = map(int, input().split())

    ok = 0
    ng = R + B

    def isOk(n):
        if n > R or n > B:
            return False

        W = (R - n) // (x - 1)
        V = (B - n) // (y - 1)

        if W + V >= n:
            return True
        return False

    while ng - ok > 1:
        mid = (ng + ok) // 2
        if isOk(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

sol()