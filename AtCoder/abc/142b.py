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
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 0
    for h in H:
        if h >= K:
            ans += 1
    print(ans)


sol()