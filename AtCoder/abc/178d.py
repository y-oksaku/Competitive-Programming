S = int(input())
MOD = 10**9 + 7

dp = [0] * (S + 1)
dp[0] = 1

for i in range(S):
    for j in range(3, S + 1):
        if i + j <= S:
            dp[i + j] = (dp[i + j] + dp[i]) % MOD
print(dp[S])
