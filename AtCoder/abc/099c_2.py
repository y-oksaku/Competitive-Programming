N = int(input())

dp = [10**18] * (N + 1)
dp[0] = 0

for i in range(N):
    # dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    prd = 6
    while i + prd <= N:
        dp[i + prd] = min(dp[i + prd], dp[i] + 1)
        prd *= 6
    prd = 9
    while i + prd <= N:
        dp[i + prd] = min(dp[i + prd], dp[i] + 1)
        prd *= 9

ans = 10**18
for i, c in enumerate(dp):
    ans = min(ans, N - i + c)
print(ans)
