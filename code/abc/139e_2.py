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

    nextGame = [deque()] + [deque(map(int, input().split())) for _ in range(N)]

    canPlay = [[False] * (N + 1) for _ in range(N + 1)]
    days = [0] * (N + 1)

    que = deque([i for i in range(1, N + 1)])

    while que:
        now = que.pop()
        if not nextGame[now]:
            continue
        enemy = nextGame[now].popleft()
        canPlay[now][enemy] = True

        if canPlay[now][enemy] and canPlay[enemy][now]:
            days[now] = days[enemy] = max(days[now], days[enemy]) + 1
            que.append(now)
            que.append(enemy)

    for a in nextGame:
        if a:
            print('-1')
            return

    ans = max(days)
    print(ans)


sol()