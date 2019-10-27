N, K = map(int, input().split())
M = (N - 1) * (N - 2) // 2

if K <= M:
    edges = []
    for i in range(2, N + 1):
        edges.append((1, i))
    dis = M - K
    for i in range(2, N + 1):
        for j in range(i + 1, N + 1):
            if dis > 0:
                edges.append((i, j))
                dis -= 1
            else:
                break
        else:
            continue
        break
    print(len(edges))
    for fr, to in edges:
        print(fr, to)
else:
    print(-1)
