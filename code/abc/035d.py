import heapq

def sol():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))

    edges = [[] for _ in range(N)]
    edgesR = [[] for _ in range(N)]
    for _ in range(M):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        edges[fr].append((to, cost))
        edgesR[to].append((fr, cost))

    minDist = [float('inf') for _ in range(N)]
    minDistR = [float('inf') for _ in range(N)]

    que = [(0, 0)]
    while que:
        dist, now = heapq.heappop(que)

        if minDist[now] < dist:
            continue

        minDist[now] = dist
        for to, cost in edges[now]:
            if minDist[to] > dist + cost:
                heapq.heappush(que, (dist + cost, to))

    que = [(0, 0)]
    while que:
        dist, now = heapq.heappop(que)

        if minDistR[now] < dist:
            continue

        minDistR[now] = dist
        for to, cost in edgesR[now]:
            if minDistR[to] > dist + cost:
                heapq.heappush(que, (dist + cost, to))

    ans = 0
    for v in range(N):
        total = (T - minDist[v] - minDistR[v]) * A[v]
        ans = max(ans, total)

    print(ans)

sol()
