N = int(input())
edges = [[] for _ in range(N)]

for i in range(N - 1):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append((i, to))
    edges[to].append((i, fr))

ans = [-1] * (N - 1)
A = [set() for _ in range(N)]

st = [0]
while st:
    now = st.pop()
    s = 1
    for i, to in edges[now]:
        if ans[i] != -1:
            continue
        while s in A[now]:
            s += 1
        ans[i] = s
        A[to].add(s)
        A[now].add(s)
        st.append(to)

print(max(ans))
print(*ans, sep="\n")
