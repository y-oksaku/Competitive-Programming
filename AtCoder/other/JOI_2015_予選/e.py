from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.buffer.readline

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
C = set([int(input()) - 1 for _ in range(K)])
edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

def getDanger():
    que = deque([(c, 0) for c in C])
    minDist = [10**18] * N

    while que:
        now, dist = que.popleft()

        if minDist[now] < dist:
            continue

        for to in edges[now]:
            if minDist[to] > dist + 1:
                minDist[to] = dist + 1
                que.append((to, dist + 1))

    return set([i for i in range(N) if minDist[i] <= S])

D = getDanger()

minDist = [10**18] * N
que = [(0, 0)]
while que:
    dist, now = heappop(que)

    if minDist[now] < dist:
        continue

    for to in edges[now]:
        if to in C:
            continue
        d = dist + (Q if to in D else P)
        if minDist[to] > d:
            minDist[to] = d
            heappush(que, (d, to))

ans = minDist[N - 1] - (Q if N - 1 in D else P)
print(ans)
