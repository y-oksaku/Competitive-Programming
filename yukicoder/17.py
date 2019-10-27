from collections import defaultdict
from heapq import heappop, heappush

N = int(input())

stopCost = [int(input()) for _ in range(N)]

M = int(input())
minDist = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    fr, to, cost = map(int, input().split())
    minDist[fr][to] = cost
    minDist[to][fr] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = minDist[i][k] + minDist[k][j]
            if minDist[i][j] > d:
                minDist[i][j] = d

ans = float('inf')
for i in range(1, N - 1):
    for j in range(i + 1, N - 1):
        dist = min(minDist[0][i] + minDist[j][N - 1], minDist[N - 1][i] + minDist[j][0]) + minDist[i][j]
        ans = min(ans, dist + stopCost[i] + stopCost[j])

print(ans)