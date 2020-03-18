import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
P = [-1] * (N + 1)

for _ in range(K):
    a, b = map(int, input().split())
    P[a] = b - 1

dp1 = [[0] * 3 for _ in range(N + 1)]
dp2 = [[0] * 3 for _ in range(N + 1)]

if P[1] != -1:
    dp1[1][P[1]] = 1
else:
    dp1[1] = [1, 1, 1]

for d, p in enumerate(P[2:], start=2):
    if p == -1:
        for i in range(3):
            dp1[d][i] = dp1[d - 1][(i + 1) % 3] + dp1[d - 1][(i + 2) % 3] + dp2[d - 1][(i + 1) % 3] + dp2[d - 1][(i + 2) % 3]
            dp2[d][i] = dp1[d - 1][i]
    else:
        dp1[d][p] = dp1[d - 1][(p + 1) % 3] + dp1[d - 1][(p + 2) % 3] + dp2[d - 1][(p + 1) % 3] + dp2[d - 1][(p + 2) % 3]
        dp2[d][p] = dp1[d - 1][p]

ans = sum(dp1[N]) + sum(dp2[N])
print(ans % 10000)
