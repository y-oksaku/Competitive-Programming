N, M = map(int, input().split())

dist = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    dist[fr][to] = 1
    dist[to][fr] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = [0] * N

for i in range(N):
    ans[i] = dist[i].count(2)

print(*ans, sep='\n')
