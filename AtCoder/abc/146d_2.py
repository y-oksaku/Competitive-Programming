N = int(input())
edges = [[] for _ in range(N)]

for i in range(N - 1):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append((i, to))
    edges[to].append((i, fr))

ans = [-1] * (N - 1)
st = [(0, -1)]
while st:
    now, pr = st.pop()

    C = []
    D = set()
    for i, _ in edges[now]:
        D.add(ans[i])
    for i in range(len(edges[now]) + 1)[::-1]:
        if i in D:
            continue
        C.append(i)

    for i, to in edges[now]:
        if to == pr:
            continue
        ans[i] = C.pop()
        st.append((to, now))

print(max(ans) + 1)
for a in ans:
    print(a + 1)
