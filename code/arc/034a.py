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

    ans = 0
    for _ in range(N):
        a, b, c, d, e = map(int, input().split())
        score = a + b + c + d + e * (110 / 900)
        ans = max(ans, score)

    print(ans)


sol()