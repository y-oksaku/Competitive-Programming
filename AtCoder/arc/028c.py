N = int(input())
edges = [[] for _ in range(N)]

for i in range(1, N):
    P = int(input())
    edges[i].append(P)
    edges[P].append(i)

order = []
parent = [0] * N
st = [0]
while st:
    now = st.pop()
    order.append(now)
    for to in edges[now]:
        if parent[now] == to:
            continue
        st.append(to)
        parent[to] = now

size = [0] * N
ans = [0] * N
for v in order[::-1]:
    size[v] += 1
    size[parent[v]] += size[v]
    for to in edges[v]:
        if to == parent[v]:
            ans[v] = max(ans[v], N - size[v])
        else:
            ans[v] = max(ans[v], size[to])
print(*ans, sep='\n')
