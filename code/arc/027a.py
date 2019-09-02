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
    h, m = map(int, input().split())

    if m == 0:
        ans = (18 - h) * 60
    else:
        ans = (17 - h) * 60 + (60 - m)

    print(ans)

sol()