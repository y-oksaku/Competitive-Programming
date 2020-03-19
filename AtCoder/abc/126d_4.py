from collections import deque
import sys
input = sys.stdin.buffer.readline

N = int(input())
INF = 10**18
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to, w = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, w))
    edges[to].append((fr, w))

dist = [INF] * N
que = deque([(0, 0)])

while que:
    now, d = que.pop()

    if dist[now] <= d:
        continue
    dist[now] = d
    for to, w in edges[now]:
        que.append((to, d + w))

ans = [dist[i] % 2 for i in range(N)]
print(*ans, sep='\n')