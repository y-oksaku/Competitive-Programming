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
    S = input().rstrip()

    if N == 1:
        print(0)
        return

    # N - 連結成分数
    # 1回の反転で，連結成分数は1または2減る
    # 反転箇所が端の場合は1でそれ以外は2
    # 中央から順に反転

    ans = 0
    for i in range(N - 1):
        if S[i] == S[i + 1] == 'R':
            ans += 1
    for i in range(1, N):
        if S[i] == S[i - 1] == 'L':
            ans += 1

    for _ in range(K):
        if ans < N - 2:
            ans += 2
        elif ans == N - 2:
            ans += 1
        elif ans == N - 1:
            break

    print(ans)

sol()