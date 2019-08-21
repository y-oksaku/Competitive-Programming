import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    x, y = map(int, input().split())
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    ans = float('inf')

    def dist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        return abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - x1 * y2)**2 / ((y2 - y1)**2 + (x2 - x1)**2)

    for i in range(N - 1):
        d = dist(points[i], points[i + 1])
        ans = min(ans, d)

    ans = min(ans, dist(points[-1], points[0]))
    print(ans**0.5)


sol()