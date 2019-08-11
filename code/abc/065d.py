import heapq

N = int(input())
cities = [0 for _ in range(N)]

for i in range(N):
    x, y = map(int, input().split())
    cities[i] = (i, x, y)

edges = [[] for _ in range(N)]

cities.sort(key=lambda A : A[1])
for i in range(N - 1):
    a, xFrom, yFrom = cities[i]
    b, xTo, yTo = cities[i + 1]
    cost = min(abs(xFrom - xTo), abs(yFrom - yTo))

    edges[a].append((cost, b))
    edges[b].append((cost, a))

cities.sort(key=lambda A : A[2])
for i in range(N - 1):
    a, xFrom, yFrom = cities[i]
    b, xTo, yTo = cities[i + 1]
    cost = min(abs(xFrom - xTo), abs(yFrom - yTo))

    edges[a].append((cost, b))
    edges[b].append((cost, a))

vertex = set([0])
newEdge = []
que = []

for cost, to in edges[0]:
    heapq.heappush(que, (cost, to))

ans = 0
while len(vertex) < N:
    cost, now = heapq.heappop(que)
    if now in vertex:
        continue
    ans += cost
    vertex.add(now)
    for c, to in edges[now]:
        if not to in vertex:
            heapq.heappush(que, (c, to))

print(ans)