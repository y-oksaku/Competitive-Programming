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
    edges = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    for edge in edges:
        if len(edge) % 2 == 1:
            print('NO')
            return

    print('YES')


sol()