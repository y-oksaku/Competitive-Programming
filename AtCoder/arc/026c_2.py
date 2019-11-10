from heapq import heappush, heappop

N, L = map(int, input().split())

edges = [[] for _ in range(L + 1)]
for i in range(1, L + 1):
    edges[i].append((i - 1, 0))

for _ in range(N):
    l, r, c = map(int, input().split())
    edges[l].append((r, c))

que = [(0, 0)]
minDist = [float('inf')] * (L + 1)
while que:
    d, now = heappop(que)
    if d >= minDist[now]:
        continue
    minDist[now] = d
    for to, cost in edges[now]:
        dist = d + cost
        if minDist[to] > dist:
            heappush(que, (dist, to))

print(minDist[L])