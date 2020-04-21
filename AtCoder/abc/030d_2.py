N, s = map(int, input().split())
K = int(input())
To = [0] + list(map(int, input().split()))

visited = [False] * (N + 1)
dist = [10**18] * (N + 1)
dist[s] = 0
now = s
D = 0
while True:
    visited[now] = True
    nx = To[now]

    if visited[nx]:
        D = dist[now] + 1 - dist[nx]
        break

    dist[nx] = dist[now] + 1
    now = nx

if dist.count(K) >= 1:
    print(dist.index(K))
    exit()

s = To[now]
K -= dist[s]
K %= D
for _ in range(K):
    s = To[s]
print(s)
