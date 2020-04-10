N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to, dist = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, dist))
    edges[to].append((fr, -dist))

INF = 10**18
minDist = [INF] * N
for s in range(N):
    if minDist[s] < INF:
        continue
    st = [s]
    minDist[s] = 0
    while st:
        now = st.pop()
        dist = minDist[now]
        for to, d in edges[now]:
            if minDist[to] == INF:
                minDist[to] = dist + d
                st.append(to)
                continue
            if minDist[to] != dist + d:
                print('No')
                exit()
print('Yes')
