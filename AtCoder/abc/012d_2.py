N, M = map(int, input().split())
INF = 10**18

minDist = [[INF] * N for _ in range(N)]
for i in range(N):
    minDist[i][i] = 0

for _ in range(M):
    fr, to, dist = map(int, input().split())
    fr -= 1
    to -= 1
    minDist[fr][to] = dist
    minDist[to][fr] = dist

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = minDist[i][k] + minDist[k][j]
            if d < minDist[i][j]:
                minDist[i][j] = d

ans = 10**18
for D in minDist:
    ans = min(max(D), ans)

print(ans)
