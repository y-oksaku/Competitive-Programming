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
    B = list(map(int, input().split()))

    A = [0] * N
    for i in range(1, N - 1):
        A[i] = min(B[i], B[i - 1])

    A[0] = B[0]
    A[-1] = B[-1]

    print(sum(A))

sol()