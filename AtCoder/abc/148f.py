from collections import deque
import sys
input = sys.stdin.readline

N, u, v = map(int, input().split())
u -= 1
v -= 1

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

def minDist(start):
    minDist = [10**10] * N
    que = deque([(start, 0, -1)])
    while que:
        now, d, pr = que.popleft()

        if minDist[now] <= d:
            continue
        minDist[now] = d

        for to in edges[now]:
            if to == pr:
                continue
            if minDist[to] > d + 1:
                que.append((to, d + 1, now))

    return minDist

minDistU = minDist(u)
minDistV = minDist(v)

ans = 0
for du, dv in zip(minDistU, minDistV):
    if du <= dv:
        ans = max(ans, dv - 1)

print(ans)