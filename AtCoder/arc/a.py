import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, A, B = map(int, input().split())
    points = [int(input()) for _ in range(N)]

    maxP = max(points)
    minP = min(points)

    if B != 0 and maxP == minP:
        print('-1')
        return

    P = B / (maxP - minP)
    newPoints = [p * P for p in points]
    avg = sum(newPoints) / N

    Q = A - avg
    print(P, Q)


sol()