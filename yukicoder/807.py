from heapq import heappop, heappush

N, M = map(int, input().split())
INF = float('inf')
isOnePath = [False] * N

edges = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append((B, C))
    edges[B].append((A, C))

minDist = [[INF] * N for _ in range(2)]
que = [(0, (0, 0))]

while que:
    dist, (now, height) = heappop(que)

    if minDist[height][now] <= dist:
        continue
    minDist[height][now] = dist

    if height == 0:
        for to, cost in edges[now]:
            if minDist[0][to] > dist + cost:
                heappush(que, (dist + cost, (to, 0)))
            if minDist[1][to] > dist:
                heappush(que, (dist, (to, 1)))
    else:
        for to, cost in edges[now]:
            if minDist[1][to] > dist + cost:
                heappush(que, (dist + cost, (to, 1)))

reverseDist = [INF] * N
que = [(0, 0)]
while que:
    dist, now = heappop(que)

    if reverseDist[now] <= dist:
        continue
    reverseDist[now] = dist

    for to, cost in edges[now]:
        if reverseDist[to] > dist + cost:
            heappush(que, (dist + cost, to))

print(0)
for i in range(1, N):
    ans = minDist[1][i] + reverseDist[i]
    print(ans)