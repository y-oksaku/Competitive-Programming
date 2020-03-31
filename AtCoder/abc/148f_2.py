N, u, v = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

def calc(s):
    minDist = [10**18] * N
    st = [(s, 0)]
    while st:
        now, dist = st.pop()

        if minDist[now] < dist:
            continue
        minDist[now] = dist

        for to in edges[now]:
            if minDist[to] > dist + 1:
                st.append((to, dist + 1))
    return minDist

distTaka = calc(u - 1)
distAoki = calc(v - 1)

ans = 0
for i in range(N):
    if distTaka[i] < distAoki[i]:
        ans = max(ans, distAoki[i] - 1)
print(ans)
