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
    tako = [list(map(int, input().split())) for _ in range(N)]

    Q = int(input())
    P = [0] * Q
    for q in range(Q):
        P[q] = int(input())

    takoSum = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(N):
            takoSum[i + 1][j + 1] = takoSum[i + 1][j] + takoSum[i][j + 1] - takoSum[i][j] + tako[i][j]

    maxTako = defaultdict(int)  # maxTako[area] = count

    for top in range(1, N + 1):
        for bottom in range(top, N + 1):
            for left in range(1, N + 1):
                for right in range(left, N + 1):
                    area = (bottom - top + 1) * (right - left + 1)
                    areaTako = takoSum[bottom][right] - takoSum[bottom][left - 1] - takoSum[top - 1][right] + takoSum[top - 1][left - 1]
                    maxTako[area] = max(maxTako[area], areaTako)

    for i in range(1, N * N):
        maxTako[i + 1] = max(maxTako[i], maxTako[i + 1])

    ans = [0] * Q
    for i, area in enumerate(P):
        ans[i] = maxTako[area]

    print(*ans, sep='\n')


sol()