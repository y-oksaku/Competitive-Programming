import sys
import heapq
from itertools import combinations
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N, M, P, Q, R = map(int, input().split())

    choco = [[] for _ in range(N)]
    for _ in range(R):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        choco[fr].append((to, cost))

    ans = 0

    for girls in combinations(range(N), P):
        boyChoco = [0] * M
        for g in girls:
            for to, cost in choco[g]:
                boyChoco[to] += cost
        boyChoco.sort(reverse=True)
        ans = max(ans, sum(boyChoco[: Q]))

    print(ans)

sol()