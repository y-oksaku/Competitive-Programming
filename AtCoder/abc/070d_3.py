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
ST = [tuple(map(lambda a: int(a) - 1, input().split())) for _ in range(Q)]


minDist = [10**18] * N
st = [(K, 0, -1)]
while st:
    now, d, pr = st.pop()
    minDist[now] = d
    for to, cost in edges[now]:
        if to == pr:
            continue
        st.append((to, d + cost, now))

ans = []
for s, t in ST:
    ans.append(minDist[s] + minDist[t])
print(*ans, sep='\n')