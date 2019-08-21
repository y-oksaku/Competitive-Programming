import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, M = map(int, input().split())

    ball = [1] * N
    hasRed = [False] * N
    hasRed[0] = True

    for _ in range(M):
        fr ,to = map(int, input().split())
        fr -= 1
        to -= 1
        if hasRed[fr]:
            hasRed[to] = True
        ball[fr] -= 1
        if ball[fr] == 0:
            hasRed[fr] = False
        ball[to] += 1

    ans = 0
    for has, count in zip(hasRed, ball):
        if has and count > 0:
            ans += 1

    print(ans)


sol()