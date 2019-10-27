from collections import deque

sX, sY, eX, eY = map(int, input().split())

N = int(input())
circles = [(sX, sY, 0)]
for _ in range(N):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))
circles.append((eX, eY, 0))

edges = [[float('inf')] * (N + 2) for _ in range(N + 2)]

for i, (x, y, r) in enumerate(circles):
    for j, (u, v, s) in enumerate(circles):
        d = max(0, ((x - u)**2 + (y - v)**2)**0.5 - (r + s))
        edges[i][j] = d

minDist = [float('inf')] * (N + 2)
confilm = [False] * (N + 2)
minDist[0] = 0
for _ in range(N + 2):
    minNode = (-1, float('inf'))
    for to in range(N + 2):
        if not confilm[to] and minDist[to] < minNode[1]:
            minNode = (to, minDist[to])
    confilm[minNode[0]] = True
    for to in range(N + 2):
        minDist[to] = min(minDist[to], minDist[minNode[0]] + edges[minNode[0]][to])

print(minDist[-1])

