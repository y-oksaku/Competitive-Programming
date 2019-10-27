import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    S = input().strip()
    N = len(S)

    A = [0] * N
    for i, s in enumerate(S):
        if s == 'D':
            A[i] = 1

    sumA = [0] * (N + 1)

    for i, a in enumerate(A):
        sumA[i + 1] = sumA[i] + a

    ans = 0
    for i in range(1, N + 1):
        lower = sumA[i - 1] * 2 + (i - 1 - sumA[i - 1])
        upper = (sumA[N] - sumA[i]) + (N - i - (sumA[N] - sumA[i])) * 2
        ans += lower + upper

    print(ans)


sol()