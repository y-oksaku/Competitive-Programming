import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    B = A.copy()
    ans = sum(B)
    minMagic = 0
    for magic in range(1, N):
        for i in range(N):
            B[i] = min(B[i], A[i - magic])
        if ans > sum(B) + X * magic:
            minMagic = magic
        ans = min(ans, sum(B) + X * magic)

    print(minMagic)
    print(ans)

sol()

