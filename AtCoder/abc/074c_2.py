A, B, C, D, E, F = map(int, input().split())
A *= 100
B *= 100

dp = [-1] * (F + 1)  # dp[f] = sugar
dp[0] = 0

for f in range(F + 1):
    if A + f <= F:
        dp[A + f] = max(dp[A + f], dp[f])
    if B + f <= F:
        dp[B + f] = max(dp[B + f], dp[f])
    if C + f <= F and dp[f] >= 0:
        water = f - dp[f]
        maxSugar = (water // 100) * E
        if dp[f] + C <= maxSugar:
            dp[C + f] = max(dp[C + f], dp[f] + C)
    if D + f <= F and dp[f] >= 0:
        water = f - dp[f]
        maxSugar = (water // 100) * E
        if dp[f] + D <= maxSugar:
            dp[D + f] = max(dp[D + f], dp[f] + D)

ans = (0, 0)
mx = -1
for f in range(1, F + 1):
    if mx < 100 * dp[f] / f:
        mx = 100 * dp[f] / f
        ans = (f, dp[f])
print(*ans)
