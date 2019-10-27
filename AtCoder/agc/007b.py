import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    P = list(map(int, input().split()))

    index = [-1] * (N + 1)
    for i, p in enumerate(P):
        index[p] = i + 1

    offset = 30000
    A = [0] * N
    B = [0] * N
    for i, p in enumerate(P):
        A[i] = index[i + 1] + offset * (i + 1)
        B[i] = offset * N - offset * i

    print(*A)
    print(*B)


sol()