from heapq import heappush, heappop

def sol():
    N, M = map(int, input().split())
    edges = [[] for _ in range(2 * N)]

    edges[0].append((N, 0))

    for _ in range(M):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        edges[fr].append((to, cost))
        edges[to].append((fr, cost))
        edges[fr + N].append((to + N, cost))
        edges[to + N].append((fr + N, cost))
        edges[fr].append((to + N, 0))
        edges[to].append((fr + N, 0))

    que = [(0, 0)]
    minDist = [float('inf')] * (2 * N)
    while que:
        dist, now = heappop(que)
        if minDist[now] < dist:
            continue
        minDist[now] = dist
        for to, cost in edges[now]:
            d = dist + cost
            if minDist[to] > d:
                heappush(que, (d, to))
                minDist[to] = d

    print(0)
    for i in range(1, N):
        print(minDist[i] + minDist[i + N])

sol()