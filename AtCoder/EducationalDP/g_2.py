import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]

    for i in range(M):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        edge[fr].append(to)

    maxLeng = [-1] * N

    def search(now):
        if maxLeng[now] != -1:
            return maxLeng[now]

        ret = 0
        for to in edge[now]:
            ret = max(ret, search(to))

        maxLeng[now] = ret + 1
        return ret + 1

    ans = 0
    for i in range(N):
        ans = max(ans, search(i))

    print(ans - 1)

sol()