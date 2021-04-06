H, W = map(int, input().split())
S = ['#' + input() + '#' for _ in range(H)]
S = ['#' * (W + 2)] + S + ['#' * (W + 2)]

MOD = 10**9 + 7

dp = [[0] * (W + 1) for _ in range(H + 1)]
accH = [[0] * (W + 1) for _ in range(H + 1)]
accW = [[0] * (W + 1) for _ in range(H + 1)]
accHW = [[0] * (W + 1) for _ in range(H + 1)]
dp[1][1] = 1
accH[1][1] = 1
accW[1][1] = 1
accHW[1][1] = 1

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if h == 1 and w == 1:
            continue
        if S[h][w] == '#':
            continue

        if S[h - 1][w] == '.':
            dp[h][w] += accH[h - 1][w]
        if S[h][w - 1] == '.':
            dp[h][w] += accW[h][w - 1]
        if S[h - 1][w - 1] == '.':
            dp[h][w] += accHW[h - 1][w - 1]

        dp[h][w] %= MOD
        accH[h][w] = (accH[h - 1][w] + dp[h][w]) % MOD
        accW[h][w] = (accW[h][w - 1] + dp[h][w]) % MOD
        accHW[h][w] = (accHW[h - 1][w - 1] + dp[h][w]) % MOD

print(dp[H][W])
