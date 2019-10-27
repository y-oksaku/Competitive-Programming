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
    H = []

    for _ in range(N):
        h = int(input())
        H.append(h)

    H.append(INF)

    mid = 0
    right = 0
    ans = 1
    for left in range(N):
        mid = max(left, mid)
        while mid < N - 1 and H[mid + 1] > H[mid]:
            mid += 1
        right = max(mid, right)
        while right < N - 1 and H[right + 1] < H[right]:
            right += 1

        ans = max(ans, right - left + 1)

    print(ans)

sol()