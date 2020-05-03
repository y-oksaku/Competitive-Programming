N, M = map(int, input().split())
H = list(map(int, input().split()))

edges = [[] for _ in range(N)]
for _ in range(M):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

ans = 0
for i, h in enumerate(H):
    mx = 0
    for to in edges[i]:
        mx = max(mx, H[to])
    if mx < h:
        ans += 1

print(ans)
