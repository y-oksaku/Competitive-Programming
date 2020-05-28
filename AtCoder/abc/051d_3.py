N, M = map(int, input().split())
INF = 10**18

minDist = [[INF] * N for _ in range(N)]
for i in range(N):
    minDist[i][i] = 0

edges = []
for _ in range(M):
    fr, to, d = map(int, input().split())
    fr -= 1
    to -= 1
    edges.append((fr, to, d))
    minDist[fr][to] = d
    minDist[to][fr] = d

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = minDist[i][k] + minDist[k][j]
            if minDist[i][j] > d:
                minDist[i][j] = d

ans = 0
for fr, to, d in edges:
    if minDist[fr][to] < d:
        ans += 1
print(ans)
