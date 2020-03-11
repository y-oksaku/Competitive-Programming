N = int(input())
P = list(map(int, input().split()))
M = P.pop()

dp = [0] * 100
dp[P[0]] = 1

for p in P[1:]:
    newDp = [0] * 100
    for i in range(21):
        if 0 <= i + p <= 20:
            newDp[i + p] += dp[i]
        if 0 <= i - p <= 20:
            newDp[i - p] += dp[i]
    dp = newDp

print(dp[M])
