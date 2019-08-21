H, W, K = map(int, input().split())
MOD = 10**9 + 7

dp = [[0 for _ in range(W)] for _ in range(H + 1)]

dp[0][0] = 1
fib = [1] * (W + 2)
for i in range(2,W+2) :
    fib[i] = fib[i - 1] + fib[i - 2]

def pat(w) :
    if w < 1 :
        return 1
    else :
        return fib[w + 1]

for i in range(H) :
    for j in range(W) :
        dp[i+1][j] = (dp[i+1][j] + dp[i][j] * pat(j - 1) * pat(W - j - 2)) % MOD
        if j > 0 :
            dp[i+1][j-1] = (dp[i+1][j-1] + dp[i][j] * pat(j - 2) * pat(W - j - 2)) % MOD
        if j <= W - 2 :
            dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j] * pat(j - 1) * pat(W - j - 3)) % MOD

print(dp[H][K-1] % MOD)