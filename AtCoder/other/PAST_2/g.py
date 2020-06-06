from collections import defaultdict, deque
from time import time

S = time()

N, X, Y = map(int, input().split())
INF = 10**9

V = set(complex(*map(int, input().split())) for _ in range(N))
D = [
    1 + 1j,
    0 + 1j,
    -1 + 1j,
    1 + 0j,
    -1 + 0j,
    0 - 1j
]

minDist = defaultdict(lambda: INF)
start = complex(0, 0)
end = complex(X, Y)

minDist[start] = 0

que = deque([start])
while que:
    if time() - S >= 1.5:
        break
    now = que.popleft()
    if now == end:
        break

    dist = minDist[now] + 1

    for d in D:
        to = d + now
        if minDist[to] <= dist or to in V:
            continue
        minDist[to] = dist
        que.append(to)

print(minDist[end] if minDist[end] < INF else -1)
