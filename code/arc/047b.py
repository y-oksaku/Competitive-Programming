import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N = int(input())
    xy = [0] * N
    uv = [0] * N  # u = x + y, v = x - y

    for i in range(N):
        x, y = map(int, input().split())
        xy[i] = (x, y)
        uv[i] = (x + y, x - y)

    top = -INF
    bottom = INF
    left = INF
    right = -INF
    for u, v in uv:
        top = max(top, v)
        bottom = min(bottom, v)
        left = min(left, u)
        right = max(right, u)

    dist = max(top - bottom, right - left)

    for centerU in [right - dist // 2, left + dist // 2]:
        for centerV in [top - dist // 2, bottom + dist // 2]:
            centerX = (centerU + centerV) // 2
            centerY = (centerU - centerV) // 2

            d = abs(centerX - xy[0][0]) + abs(centerY - xy[0][1])
            for x, y in xy:
                if d != abs(centerX - x) + abs(centerY - y):
                    break
            else:
                print(centerX, centerY)
                return

sol()