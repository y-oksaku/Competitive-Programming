def sol():
    N, M = map(int, input().split())

    minDist = [[float('inf') for _ in range(N)] for _ in range(N)]
    edges = set([])

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        minDist[a][b] = c
        minDist[b][a] = c
        edges.add((min(a, b), max(a, b)))

    noEdge = set([])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if minDist[i][j] > minDist[i][k] + minDist[k][j]:
                    minDist[i][j] = minDist[i][k] + minDist[k][j]
                    noEdge.add((min(i, j), max(i, j)))

    nessEdge = edges - noEdge
    print(M - len(nessEdge))

sol()