from heapq import heappop, heappush

N, M = map(int, input().split())
INF = 10**10

edges = [[] for _ in range(N * 3)]

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to + N)
    edges[fr + N].append(to + 2 * N)
    edges[fr + 2 * N].append(to)

S, T = map(int, input().split())
S -= 1
T -= 1

minDist = [INF] * (3 * N)
que = [(0, S)]

while que:
    dist, now = heappop(que)

    if minDist[now] <= dist:
        continue
    minDist[now] = dist

    dist += 1

    for to in edges[now]:
        if minDist[to] > dist:
            heappush(que, (dist, to))

ans = minDist[T]

if ans == INF:
    print(-1)
else:
    print(ans // 3)