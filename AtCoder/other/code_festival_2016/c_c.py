import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if T[-1] != A[0]:
        print(0)
        return

    minHeight = [float('inf')] * N
    minHeight[0] = -1
    minHeight[N - 1] = -1

    for i in range(1, N - 1):
        if T[i] > T[i - 1]:
            if T[i] > A[i]:
                print(0)
                return
            minHeight[i] = -1
        if A[i] > A[i + 1]:
            if A[i] > T[i]:
                print(0)
                return
            minHeight[i] = -1
        minHeight[i] = min(minHeight[i], A[i], T[i])

    ans = 1
    for h in minHeight:
        if h == -1:
            continue
        ans = (ans * h) % MOD

    print(ans)

sol()