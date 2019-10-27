import sys
input = sys.stdin.readline
INF = float('inf')

N, M, L = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
ST = [tuple(map(int, input().split())) for _ in range(Q)]

dist = [[INF] * N for _ in range(N)]
fuel = [[INF] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0
    fuel[i][i] = 0

for fr, to, cost in ABC:
    if cost > L:
        continue
    fr -= 1
    to -= 1
    dist[fr][to] = cost
    dist[to][fr] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = dist[i][k] + dist[k][j]
            if dist[i][j] > d:
                dist[i][j] = d
            if d <= L:
                fuel[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = fuel[i][k] + fuel[k][j]
            if fuel[i][j] > d:
                fuel[i][j] = d

for start, end in ST:
    print(fuel[start - 1][end - 1] - 1 if fuel[start - 1][end - 1] != INF else -1)
