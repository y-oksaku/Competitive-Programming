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

minDist = [10**18] * N
minDist[K] = 0
st = [(K, 0)]
while st:
    now, dist = st.pop()
    for to, c in edges[now]:
        d = dist + c
        if minDist[to] > d:
            minDist[to] = d
            st.append((to, d))

ans = []
for _ in range(Q):
    X, Y = map(lambda a: int(a) - 1, input().split())
    ans.append(minDist[X] + minDist[Y])

print(*ans, sep='\n')
