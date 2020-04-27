from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
C = set()

edges = [[] for _ in range(N)]
for _ in range(M):
    fr, to, c = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, c))
    edges[to].append((fr, c))
    C.add(c)

minDist = [10**18] * (N + 1)
minDistList = [set() for _ in range(N)]
minDistList[0] = C

que = [(1, 0, 0)]
while que:
    dist, f, now = heappop(que)

    for to, c in edges[now]:
        d = dist
        if not c in minDistList[now]:
            d += 1
        if minDist[to] > d:
            minDist[to] = d
            minDistList[to] = set()
            heappush(que, (d, f + 1, to))
        if minDist[to] == d:
            minDistList[to].add(c)

for _ in range(2):
    que = [(minDist[i], 0, i) for i in range(N)]
    heapify(que)
    while que:
        dist, f, now = heappop(que)

        for to, c in edges[now]:
            d = dist
            if not c in minDistList[now]:
                d += 1
            if minDist[to] > d:
                minDist[to] = d
                minDistList[to] = set()
                heappush(que, (d, f + 1, to))
            if minDist[to] == d:
                minDistList[to].add(c)

ans = minDist[N - 1]
print(ans if ans < 10**18 else -1)
