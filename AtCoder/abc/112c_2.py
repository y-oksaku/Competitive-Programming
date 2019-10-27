import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points.sort(key=itemgetter(2), reverse=True)

    for cx in range(101):
        for cy in range(101):
            bx, by, bh = points[0]
            H = bh + abs(cx - bx) + abs(cy - by)
            for x, y, h in points:
                nowH = max(H - abs(cx - x) - abs(cy - y), 0)
                if h != nowH:
                    break
            else:
                print(cx, cy, H)
                return

sol()