from collections import deque

N = int(input())

edge = [[] for _ in range(N)]
check = [False] * N
dist = [0] * N

for i in range(N-1) :
    u , v , w = map(int,input().split())
    edge[u-1].append((v-1,w))
    edge[v-1].append((u-1,w))

q = deque([0])

while q :
    current = q.popleft()
    if check[current] :
        continue

    check[current] = True
    for ad , w in edge[current] :
        if not check[ad] :
            q.append(ad)
            dist[ad] = dist[current] + w

for w in dist :
    print(w % 2)