N, M = map(int, input().split())
minDist = [[float('inf') for _ in range(N)] for _ in range(N)]
backEdge = []

for _ in range(M):
    fr, to, cost = map(int, input().split())
    fr -= 1
    to -= 1
    if fr == 0 or to == 0:
        fr, to = min(fr, to), max(fr, to)
        backEdge.append((fr, to, cost))
    else:
        minDist[fr][to] = cost
        minDist[to][fr] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            if minDist[i][j] > minDist[i][k] + minDist[k][j]:
                minDist[i][j] = minDist[i][k] + minDist[k][j]

ans = float('inf')
for i in range(len(backEdge)):
    for j in range(i + 1, len(backEdge)):
        length = backEdge[i][2] + minDist[backEdge[i][1]][backEdge[j][1]] + backEdge[j][2]
        ans = min(ans, length)

if ans == float('inf'):
    print('-1')
else:
    print(ans)