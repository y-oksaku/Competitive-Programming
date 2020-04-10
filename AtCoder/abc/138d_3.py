N, Q = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

ans = [0] * (N + 1)

for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

st = [(0, N)]
while st:
    now, pr = st.pop()

    ans[now] += ans[pr]
    for to in edges[now]:
        if to == pr:
            continue
        st.append((to, now))
print(*ans[:N])
