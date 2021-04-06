from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for P in permutations(range(1, N), r=N - 1):
    cost = T[0][P[0]] + T[P[-1]][0]
    for p1, p2 in zip(P, P[1:]):
        cost += T[p1][p2]

    if cost == K:
        ans += 1

print(ans)
