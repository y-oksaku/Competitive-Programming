from collections import deque

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))

ans = 0
for removeEdge in range(M):
    confilm = [False for _ in range(N)]
    que = deque([])
    que.append(0)

    while que:
        now = que.popleft()
        confilm[now] = True
        for i, (a, b) in enumerate(edges):
            if i == removeEdge:
                continue
            if a == now:
                if not confilm[b]:
                    que.append(b)
            if b == now:
                if not confilm[a]:
                    que.append(a)
    if False in confilm:
        ans += 1

print(ans)