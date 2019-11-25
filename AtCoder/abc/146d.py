from collections import deque

N = int(input())

edges = [[] for _ in range(N + 1)]
for i in range(N - 1):
    fr, to = map(int, input().split())
    edges[fr].append((to, i))
    edges[to].append((fr, i))

que = deque([(1, -1)])
ans = [-1] * (N - 1)
while que:
    now, parent = que.popleft()

    canUse = set(range(1, len(edges[now]) + 1))
    for to, i in edges[now]:
        if to == parent and ans[i] in canUse:
            canUse.remove(ans[i])

    canUse = list(canUse)
    for to, i in edges[now]:
        if to == parent:
            continue
        color = canUse.pop()
        if ans[i] == -1:
            ans[i] = color
        que.append((to, now))

print(max(ans))
print(*ans, sep='\n')
