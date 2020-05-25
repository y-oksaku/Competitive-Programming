from collections import deque

N, M, P = map(int, input().split())

edges = [[] for _ in range(N)]
revEdges = [[] for _ in range(N)]
E = []
for _ in range(M):
    fr, to, cost = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    revEdges[to].append(fr)
    E.append((fr, to, -(cost - P)))

def canVisit(start, edges):
    st = deque([start])
    minDist = [10**18] * N
    minDist[start] = 0

    while st:
        now = st.popleft()
        d = minDist[now] + 1
        for to in edges[now]:
            if minDist[to] > d:
                minDist[to] = d
                st.append(to)

    return [True if minDist[to] < 10**18 else False for to in range(N)]

canForward = canVisit(0, edges)
canBack = canVisit(N - 1, revEdges)

minDist = [10**18] * N
minDist[0] = 0
for i in range(N + 1):
    for fr, to, cost in E:
        d = minDist[fr] + cost
        if minDist[to] > d:
            if i == N and canForward[fr] and canBack[to]:
                print(-1)
                exit()

            minDist[to] = d

print(max(0, -minDist[N - 1]))
