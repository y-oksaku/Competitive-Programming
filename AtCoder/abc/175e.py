R, C, K = map(int, input().split())

items = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    items[r - 1][c - 1] = v

dp0 = [[0] * (C + 1) for _ in range(R + 1)]
dp1 = [[0] * (C + 1) for _ in range(R + 1)]
dp2 = [[0] * (C + 1) for _ in range(R + 1)]
dp3 = [[0] * (C + 1) for _ in range(R + 1)]

for r in range(R):
    for c in range(C):
        v = items[r][c]
        for fr, to in ((dp2, dp3), (dp1, dp2), (dp0, dp1)):
            to[r][c] = max(to[r][c], fr[r][c] + v)

        for dp in (dp0, dp1, dp2, dp3):
            dp[r][c + 1] = max(dp[r][c + 1], dp[r][c])
            dp0[r + 1][c] = max(dp0[r + 1][c], dp[r][c])

ans = max(
    dp0[R - 1][C], dp0[R][C - 1],
    dp1[R - 1][C], dp1[R][C - 1],
    dp2[R - 1][C], dp2[R][C - 1],
    dp3[R - 1][C], dp3[R][C - 1],
)

print(ans)
