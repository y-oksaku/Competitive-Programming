import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]

    confilm = [False] * N
    for a in reversed(A):
        if confilm[a - 1]:
            continue
        print(a)
        confilm[a - 1] = True

    for i in range(1, N + 1):
        if confilm[i - 1]:
            continue
        print(i)

sol()