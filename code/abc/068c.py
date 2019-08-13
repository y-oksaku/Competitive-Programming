from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(start, end):
    minDist = [-1 for _ in range(N)]
    minDist[start] = 0

    que = deque([])
    que.append((start, 0))

    while que:
        now, dist = que.popleft()

        minDist[now] = dist
        if now == end:
            return dist

        for to in edges[now]:
            if minDist[to] >= 0:
                continue
            que.append((to, dist + 1))

    return float('inf')

if dfs(0, N - 1) <= 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')