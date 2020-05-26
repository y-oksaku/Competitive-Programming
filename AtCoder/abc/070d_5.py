N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to, cost = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, cost))
    edges[to].append((fr, cost))

Q, K = map(int, input().split())
K -= 1
XY = [tuple(map(lambda a: int(a) - 1, input().split())) for _ in range(Q)]

minDist = [10**18] * N
minDist[K] = 0
st = [K]
while st:
    now = st.pop()
    dist = minDist[now]
    for to, c in edges[now]:
        d = dist + c
        if minDist[to] > d:
            minDist[to] = d
            st.append(to)

ans = [minDist[x] + minDist[y] for x, y in XY]
print(*ans, sep='\n')
