from heapq import heappush, heappop

N, M, P, Q, T = map(int, input().split())
P -= 1
Q -= 1

edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to, cost = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, cost))
    edges[to].append((fr, cost))

def minDist(s):
    dist = [float('inf')] * N
    dist[s] = 0
    que = [(0, s)]
    while que:
        d, now = heappop(que)
        for to, cost in edges[now]:
            nd = d + cost
            if dist[to] > nd:
                dist[to] = nd
                heappush(que, (nd, to))
    return dist

minDistS = minDist(0)
minDistP = minDist(P)
minDistQ = minDist(Q)

ans = -1

if minDistS[P] + minDistP[Q] + minDistQ[0] <= T or minDistS[Q] + minDistQ[P] + minDistP[0] <= T:
    ans = T

for s in range(N):
    for t in range(N):
        time = minDistS[s] + max(minDistP[s] + minDistP[t], minDistQ[s] + minDistQ[t]) + minDistS[t]
        if time <= T:
            ans = max(ans, T - time + minDistS[s] + minDistS[t])

print(ans)
