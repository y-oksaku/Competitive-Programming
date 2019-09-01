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
    H = list(map(int, input().split()))

    ans = 0
    now = 0
    for i in range(N):
        if i + 1 < N and H[i + 1] <= H[i]:
            now += 1
            ans = max(ans, now)
        else:
            now = 0

    print(ans)

sol()