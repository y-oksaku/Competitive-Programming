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

    A = [0] * N
    centerA = [0, 0]

    for i in range(N):
        x, y = map(int, input().split())
        A[i] = (x, y)
        centerA[0] += x
        centerA[1] += y
    centerA[0] = centerA[0] / N
    centerA[1] = centerA[1] / N

    B = [0] * N
    centerB = [0, 0]
    for i in range(N):
        x, y = map(int, input().split())
        B[i] = (x, y)
        centerB[0] += x
        centerB[1] += y
    centerB[0] = centerB[0] / N
    centerB[1] = centerB[1] / N

    maxDistA = 0
    for x, y in A:
        maxDistA = max(maxDistA, (centerA[0] - x)**2 + (centerA[1] - y)**2)
    maxDistB = 0
    for x, y in B:
        maxDistB = max(maxDistB, (centerB[0] - x)**2 + (centerB[1] - y)**2)

    P2 = maxDistB / maxDistA

    print(P2**0.5)

sol()