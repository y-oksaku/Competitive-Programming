from itertools import permutations

N, M, R = map(int, input().split())
R = list(map(lambda a: int(a) - 1, input().split()))

minDist = [[10**18] * N for _ in range(N)]
for _ in range(M):
    fr, to, cost = map(int, input().split())
    fr -= 1
    to -= 1
    minDist[fr][to] = cost
    minDist[to][fr] = cost
for i in range(N):
    minDist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = minDist[i][k] + minDist[k][j]
            if minDist[i][j] > d:
                minDist[i][j] = d

ans = 10**18
for P in permutations(R, r=len(R)):
    cost = 0
    for fr, to in zip(P, P[1:]):
        cost += minDist[fr][to]
    ans = min(ans, cost)
print(ans)
