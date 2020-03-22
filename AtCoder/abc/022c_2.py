N, M = map(int, input().split())
INF = 10**18
minDist = [[INF] * N for _ in range(N)]
D = [INF] * N

for i in range(N):
    minDist[i][i] = 0

for _ in range(M):
    fr, to, dist = map(int, input().split())
    fr -= 1
    to -= 1
    if min(fr, to) == 0:
        D[max(fr, to)] = dist
    else:
        minDist[fr][to] = dist
        minDist[to][fr] = dist

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = minDist[i][k] + minDist[k][j]
            if minDist[i][j] > d:
                minDist[i][j] = d

ans = INF
for s in range(N):
    for t in range(s + 1, N):
        d = D[s] + minDist[s][t] + D[t]
        ans = min(ans, d)

print(ans if ans < INF else -1)