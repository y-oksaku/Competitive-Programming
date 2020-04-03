from heapq import heappop, heappush

N, M, S, T = map(int, input().split())
K = 10**15
S -= 1
T -= 1

edgesYen = [[] for _ in range(N)]
edgesSun = [[] for _ in range(N)]

for _ in range(M):
    fr, to, yen, sun = map(int, input().split())
    fr -= 1
    to -= 1
    edgesYen[fr].append((to, yen))
    edgesYen[to].append((fr, yen))
    edgesSun[fr].append((to, sun))
    edgesSun[to].append((fr, sun))

def calcMinDist(edges, start):
    minDist = [10**18] * N
    minDist[start] = 0
    que = [(0, start)]
    while que:
        dist, now = heappop(que)

        if minDist[now] < dist:
            continue

        for to, d in edges[now]:
            if minDist[to] > dist + d:
                heappush(que, (dist + d, to))
                minDist[to] = dist + d

    return minDist

minDistYenS = calcMinDist(edgesYen, S)
minDistSunT = calcMinDist(edgesSun, T)

ans = [0] * N
for mid in range(N):
    ans[mid] = K - minDistYenS[mid] - minDistSunT[mid]

for mid in range(N - 1)[::-1]:
    ans[mid] = max(ans[mid], ans[mid + 1])

print(*ans, sep='\n')
