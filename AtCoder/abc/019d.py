import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N = int(input())

    rootDist = [0] * N

    for i in range(1, N):
        print('? {} {}'.format(1, i + 1), flush=True)
        rootDist[i] = int(input())

    p = 0
    for i in range(N):
        if rootDist[p] < rootDist[i]:
            p = i

    ans = rootDist[p]
    for i in range(N):
        if i == p:
            continue
        print('? {} {}'.format(p + 1, i + 1), flush=True)
        ans = max(ans, int(input()))

    print('! {}'.format(ans))

sol()