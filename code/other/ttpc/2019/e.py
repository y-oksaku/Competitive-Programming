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

    if N == 1:
        print('Yes')
        print('1')
        return

    if N % 2 == 0:
        print('No')
        return

    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i][j] = i + j * N

    ans[0][0] = N**2

    for i in range(N):
        ans[i][i], ans[0][i] = ans[0][i], ans[i][i]

    for i in range(N):
        ans[i][i], ans[i][0] = ans[i][0], ans[i][i]

    print('Yes')
    for a in ans:
        print(*a)

sol()