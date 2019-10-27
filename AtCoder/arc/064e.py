sX, sY, eX, eY = map(int, input().split())
N = int(input())

circles = [(sX, sY, 0)]
for _ in range(N):
    cx, cy, r = map(int, input().split())
    circles.append((cx, cy, r))
circles.append((eX, eY, 0))

edges = [[float('inf')] * (N + 2) for _ in range(N + 2)]

for i, (cx1, cy1, r1) in enumerate(circles):
    for j, (cx2, cy2, r2) in enumerate(circles):
        cDist = ((cx1 - cx2)**2 + (cy1 - cy2)**2)**0.5
        dist = max(0, cDist - r1 - r2)

        edges[i][j] = dist
        edges[j][i] = dist

minDist = [float('inf')] * (N + 2)
minDist[0] = 0
confilm = [False] * (N + 2)

for _ in range(N + 2):
    md = float('inf')
    minNode = -1
    for n in range(N + 2):
        if not confilm[n] and md > minDist[n]:
            minNode = n
            md = minDist[n]
    confilm[minNode] = True
    for to in range(N + 2):
        minDist[to] = min(minDist[to], minDist[minNode] + edges[minNode][to])

print(minDist[-1])
