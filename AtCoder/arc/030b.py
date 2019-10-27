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
    N, X = map(int, input().split())
    H = list(map(int, input().split()))
    X -= 1

    edges = [[] for _ in range(N)]

    for _ in range(N - 1):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        edges[fr].append(to)
        edges[to].append(fr)

    def seach(now, prev):
        if edges[now] == [prev]:
            return H[now]

        ret = 0
        for to in edges[now]:
            if to == prev:
                continue
            ret += seach(to, now)

        if ret > 0:
            return ret + 1
        else:
            return H[now]

    ans = seach(X, -1) - 1
    if ans < 0:
        print(0)
    else:
        print(ans * 2)

sol()