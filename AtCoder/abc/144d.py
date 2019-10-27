import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')
EPS = 1e-8

from math import tan, degrees, pi, atan2

def sol():
    a, b, x = map(int, input().split())
    deg1 = atan2(b, a)

    def isOk(deg):
        if deg > deg1:
            z = min(a, b / tan(deg))
            value = b * z * a / 2
            if x <= value:
                return True
            else:
                return False
        else:
            deg = pi / 2 - deg
            z = min(b, a / tan(deg))
            value = a * a * b - (z * a * a / 2)
            if x <= value:
                return True
            else:
                return False

    ok = 0.0
    ng = pi / 2

    while abs(ok - ng) > EPS:
        mid = (ok + ng) / 2
        if isOk(mid):
            ok = mid
        else:
            ng = mid

    print(degrees(ok))

sol()