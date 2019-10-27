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
    S = input().rstrip()

    ans = 0
    prev = -1

    for s in S:
        if prev != s:
            ans += 1
            prev = s

    print(ans)

sol()