N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

def calc(s):
    minDist = [10**18] * N
    st = [(s, -1)]
    minDist[s] = 0
    while st:
        now, pr = st.pop()
        for to in edges[now]:
            if to == pr:
                continue
            minDist[to] = minDist[now] + 1
            st.append((to, now))
    return minDist

A = calc(0)
S = A.index(max(A))

B = calc(S)
T = B.index(max(B))

print(S + 1, T + 1)
