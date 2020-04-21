N = int(input())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)
C = list(map(int, input().split()))
A = sum(C) - max(C)
C.sort()

ans = [None] * N
ans[0] = C.pop()
st = [0]
while st:
    now = st.pop()
    for to in edges[now]:
        if ans[to] == None:
            ans[to] = C.pop()
            st.append(to)

print(A)
print(*ans)
