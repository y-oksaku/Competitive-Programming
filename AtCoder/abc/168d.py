from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(M):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

ans = [-1] * N
minDist = [10**18] * N
minDist[0] = 0
que = deque([0])

while que:
    now = que.popleft()
    dist = minDist[now] + 1
    for to in edges[now]:
        if minDist[to] > dist:
            minDist[to] = dist
            ans[to] = now
            que.append(to)

print('Yes')
for a in ans[1:]:
    print(a + 1)
