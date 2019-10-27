N = int(input())
C = [int(input()) for _ in range(N)]
MOD = 10**9 + 7

dp = [0] * (N + 1)
colorToIndex = [-1] * (max(C) + 10)
colorToIndex[C[0]] = 0
dp[0] = 1

for i, color in enumerate(C[1:], start=1):
    prevIndex = colorToIndex[color]
    dp[i] = dp[i - 1]

    if prevIndex != i - 1:
        dp[i] += dp[prevIndex]

    dp[i] %= MOD
    colorToIndex[color] = i

ans = dp[N - 1]
print(ans)
