from collections import deque

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

que = deque([])
que.append((0, 0))

minDist = [float('inf') for _ in range(N)]

while que:
    now, dist = que.popleft()

    if minDist[now] <= dist:
        continue
    minDist[now] = dist

    for to in edges[now]:
        if dist + 1 < minDist[to]:
            que.append((to, dist + 1))

now = N - 1
minPath = [now]
dist = minDist[N - 1]
while dist > 0:
    for back in edges[now]:
        if minDist[back] == dist - 1:
            minPath.append(back)
            dist -= 1
            now = back
            break

edges[minPath[len(minPath) // 2]].remove(minPath[len(minPath) // 2 - 1])
edges[minPath[len(minPath) // 2 - 1]].remove(minPath[len(minPath) // 2])

confilm = [0 for _ in range(N)]
que.clear()
que.append(0)

while que:
    now = que.popleft()

    confilm[now] = 1

    for to in edges[now]:
        if confilm[to] == 0:
            que.append(to)

blackCount = sum(confilm)
witeCount = N - blackCount

if blackCount > witeCount:
    print('Fennec')
else:
    print('Snuke')