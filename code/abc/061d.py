from collections import deque

N, M = map(int, input().split())

edges = []
dfsEdges = [[] for _ in range(N)]
dfsReverseEdges = [[] for _ in range(N)]

for _ in range(M):
    back, to, cost = map(int, input().split())
    back -= 1
    to -= 1
    edges.append((back, to, -cost))

    dfsEdges[back].append(to)
    dfsReverseEdges[to].append(back)

minDist = [float('inf') for _ in range(N)]
minDist[0] = 0

canGo = [False for _ in range(N)]
canBack = [False for _ in range(N)]

canGo[0] = True
canBack[N - 1] = True

def dfs(start, edge, confilm):
    que = deque([])
    que.append(start)

    while que:
        now = que.pop()
        for to in edge[now]:
            if not confilm[to]:
                que.append(to)
                confilm[to] = True

dfs(0, dfsEdges, canGo)
dfs(N - 1, dfsReverseEdges, canBack)

for time in range(N):
    for back, to, cost in edges:
        if minDist[to] > minDist[back] + cost:
            minDist[to] = minDist[back] + cost
            if time == N - 1:
                if canGo[to] and canBack[to]:
                    print('inf')
                    exit(0)

print(-minDist[N - 1])