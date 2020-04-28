N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to, dist = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, dist))
    edges[to].append((fr, -dist))

def isOk():
    visited = [False] * N
    INF = 10**18
    minDist = [INF] * N
    for s in range(N):
        if visited[s]:
            continue
        st = [(s, 0)]
        minDist[s] = 0
        visited[s] = True
        while st:
            now, dist = st.pop()

            for to, d in edges[now]:
                d += dist
                if visited[to]:
                    if minDist[to] != d:
                        return False
                else:
                    visited[to] = True
                    minDist[to] = d
                    st.append((to, d))
    return True

print('Yes' if isOk() else 'No')
