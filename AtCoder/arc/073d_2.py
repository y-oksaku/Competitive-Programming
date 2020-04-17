N, W = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in range(N)]
R = 3 * N + 10
INF = 10**18

w0 = WV[0][0]

dp = [[-INF] * R for _ in range(N + 1)]
dp[0][0] = 0

for w, v in WV:
    k = w - w0
    for n in range(N)[::-1]:
        for r in range(R)[::-1]:
            if r + k < R and dp[n + 1][r + k] < dp[n][r] + v:
                dp[n + 1][r + k] = dp[n][r] + v

ans = 0
for n in range(N + 1):
    for r in range(R):
        w = n * w0 + r
        if w <= W and dp[n][r] > ans:
            ans = dp[n][r]
print(ans)
