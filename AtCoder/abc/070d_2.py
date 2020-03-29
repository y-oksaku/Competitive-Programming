from collections import deque
import sys
input = sys.stdin.buffer.readline

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
XY = [tuple(map(int, input().split())) for _ in range(Q)]

que = deque([(K, -1, 0)])
dist = [10**18] * N
while que:
    now, pr, d = que.popleft()
    dist[now] = d
    for to, c in edges[now]:
        if to == pr:
            continue
        que.append((to, now, d + c))

ans = [dist[x - 1] + dist[y - 1] for x, y in XY]
print(*ans, sep='\n')
