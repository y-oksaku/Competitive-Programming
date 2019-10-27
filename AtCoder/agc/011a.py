import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, C, K = map(int, input().split())
    T = [0] * N

    for i in range(N):
        T[i] = int(input())

    T.sort(reverse=True)
    ans = 0

    nowTime = float('inf')
    nowCount = 0
    for t in T:
        if nowTime - K <= t and nowCount < C:
            nowCount += 1
            continue
        ans += 1
        nowTime = t
        nowCount = 1

    print(ans)

sol()