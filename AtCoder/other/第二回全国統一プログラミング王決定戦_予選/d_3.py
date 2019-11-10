from heapq import heappush, heappop

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for i in range(1, N):
    edges[i].append((i - 1, 0))

for _ in range(M):
    l, r, c = map(int, input().split())
    l -= 1
    r -= 1
    edges[l].append((r, c))

que = [(0, 0)]
minDist = [float('inf')] * N
while que:
    d, now = heappop(que)
    if d >= minDist[now]:
        continue
    minDist[now] = d
    for to, cost in edges[now]:
        dist = d + cost
        if minDist[to] > dist:
            heappush(que, (dist, to))

ans = minDist[N - 1]
print(-1 if ans == float('inf') else ans)