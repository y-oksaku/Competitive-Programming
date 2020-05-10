N, K = map(int, input().split())
A = list(map(lambda a: int(a) - 1, input().split()))
INF = 10**18

minDist = [INF] * N
minDist[0] = 0

now = 0
R = 0
while minDist[now] < INF:
    to = A[now]
    if minDist[to] < INF:
        R = minDist[now] + 1 - minDist[to]
        break
    minDist[to] = minDist[now] + 1
    now = to

if minDist.count(K) > 0:
    print(minDist.index(K) + 1)
    exit()

K -= minDist[now]
M = K % R
for _ in range(M):
    now = A[now]
print(now + 1)