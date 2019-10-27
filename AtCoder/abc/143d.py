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
    L = list(map(int, input().split()))
    L.sort()

    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            A = L[i]
            B = L[j]

            minC = max(A - B, B - A)
            maxC = A + B

            left = bisect_right(L, minC)
            right = bisect_left(L, maxC)

            ans += right - left

            if left <= i < right:
                ans -= 1
            if left <= j < right:
                ans -= 1

    print(ans // 6)


sol()