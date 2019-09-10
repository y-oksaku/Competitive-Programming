from collections import deque

N = int(input())

edges = [[] for _ in range(N)]
edgeList = []
for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)
    edgeList.append((fr, to))

C = list(map(int, input().split()))
C.sort()

M = sum(C) - C[-1]

values = [-1] * N
que = deque([0])

while que:
    now = que.popleft()
    values[now] = C.pop()
    for to in edges[now]:
        if values[to] == -1:
            que.append(to)

print(M)
print(*values)