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
    N, M = map(int, input().split())

    ism = [0] * (N + 1)
    A = []

    for _ in range(M):
        s, t = map(int, input().split())
        s -= 1
        A.append((s, t))
        ism[s] += 1
        ism[t] -= 1

    for i in range(1, N + 1):
        ism[i] += ism[i - 1]

    canDelete = [0] * (N + 1)

    for i in range(N):
        if ism[i] <= 1:
            canDelete[i + 1] = -1

    for i in range(1, N + 1):
        canDelete[i] += canDelete[i - 1]

    ans = []
    for i, (s, t) in enumerate(A):
        if canDelete[t] - canDelete[s] == 0:
            ans.append(i + 1)

    print(len(ans))
    if ans:
        print(*ans, sep='\n')

sol()