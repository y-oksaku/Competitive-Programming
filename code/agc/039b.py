N = int(input())

dist = [[1 if s == '1' else float('inf') for s in input()] for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

baseMod = [d % 2 for d in dist[0]]

for i in range(N):
    A = [0] * N
    for j, d in enumerate(dist[i]):
        A[j] = (d + baseMod[i]) % 2
    if A != baseMod:
        print(-1)
        exit()

ans = max([max(D) for D in dist]) + 1
print(ans)