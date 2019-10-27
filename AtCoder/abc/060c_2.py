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
    N, T = map(int, input().split())
    push = list(map(int, input().split())) + [INF]

    ans = 0
    for i in range(N):
        ans += min(T, push[i + 1] - push[i])

    print(ans)


sol()