N, M, Q = map(int, input().split())

LR = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    L, R = map(int, input().split())
    LR[L][R] += 1

for l in range(1, N + 1):
    for r in range(1, N + 1):
        LR[l][r] = LR[l - 1][r] + LR[l][r - 1] - LR[l - 1][r - 1] + LR[l][r]

ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    cnt = LR[q][q] - LR[q][p - 1] - LR[p - 1][q] + LR[p - 1][p - 1]
    ans.append(cnt)

print(*ans, sep='\n')