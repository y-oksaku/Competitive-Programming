N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to, d = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, d))
    edges[to].append((fr, d))

minDist = [10**18] * N
st = [(0, 0)]
while st:
    now, dist = st.pop()

    if minDist[now] < dist:
        continue
    minDist[now] = dist

    for to, d in edges[now]:
        if minDist[to] > dist + d:
            st.append((to, dist + d))

for i in range(N):
    print(0 if minDist[i] % 2 == 0 else 1)
