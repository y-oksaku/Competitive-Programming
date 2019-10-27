from collections import deque

N = int(input())
C = int(input())
V = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))
Y = list(map(int, input().split()))
M = list(map(int, input().split()))

edges = [[] for _ in range(N)]

for fr, to, cost, time in zip(S, T, Y, M):
    fr -= 1
    to -= 1
    edges[fr].append((to, cost, time))

que = deque([(0, 0, 0)])
minDist = [(float('inf'), float('inf'))] * N
ans = float('inf')
while que:
    now, cost, time = que.popleft()

    if minDist[now][0] <= cost and minDist[now][1] <= time:
        continue
    elif minDist[now][0] > cost and minDist[now][1] > time:
        minDist[now] = (cost, time)

    if now == N - 1:
        ans = min(ans, time)
        continue

    for to, c, t in edges[now]:
        if c + cost > C or (minDist[to][0] <= cost and minDist[to][1] <= time):
            continue
        que.append((to, c + cost, time + t))

if ans == float('inf'):
    print(-1)
else:
    print(ans)
