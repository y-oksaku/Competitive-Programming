N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

def isBipartite():
    sign = [-1] * N
    sign[0] = 0
    st = [0]
    while st:
        now = st.pop()
        p = sign[now]

        for to in edges[now]:
            if sign[to] == -1:
                st.append(to)
                sign[to] = (p + 1) % 2
                continue
            if sign[to] != (p + 1) % 2:
                return -1

    return sum(sign)

s = isBipartite()

if s == -1:
    print(N * (N - 1) // 2 - M)
else:
    print(s * (N - s) - M)
