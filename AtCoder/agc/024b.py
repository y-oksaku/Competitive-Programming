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
    P = [0] * N

    for i in range(N):
        P[i] = int(input())

    pToIndex = {p : i for i, p in enumerate(P)}

    maxLeng = 1
    length = 1
    for n in range(1, N):
        if pToIndex[n] < pToIndex[n + 1]:
            length += 1
            maxLeng = max(maxLeng, length)
        else:
            length = 1

    print(N - maxLeng)

sol()