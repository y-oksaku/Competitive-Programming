W, H = map(int, input().split())
MOD = 10**9 + 7

dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
dp[0][0] = 1

for h in range(H):
    for w in range(W):
        dp[h + 1][w] = (dp[h + 1][w] + dp[h][w]) % MOD
        dp[h][w + 1] = (dp[h][w + 1] + dp[h][w]) % MOD

print(dp[H - 1][W - 1])