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
    A = [deque()] + [deque(map(int, input().split())) for _ in range(N)]

    days = [0] * (N + 1)
    now = [0] * (N + 1)

    que = deque([i + 1 for i in range(N)])

    while que:
        i = que.popleft()
        if not A[i]:
            continue

        a = A[i].popleft()
        if now[a] == i:
            days[a] = days[i] = max(days[a], days[i]) + 1
            que.append(i)
            que.append(a)
            now[a] = now[i] = 0
        else:
            now[i] = a

    for i in range(1, N + 1):
        if A[i]:
            print(-1)
            return
    print(max(days))


sol()