N, K = map(int, input().split())
MOD = 998244353
S = []

for _ in range(K):
    l, r = map(int, input().split())
    S.append((l, r))

dp = [0] * (N + 1)
accDp = [0] * (N + 1)
dp[1] = 1
accDp[1] = 1

for i in range(2, N + 1):
    for l, r in S:
        r, l = max(0, i - l), max(1, i - r)
        dp[i] += accDp[r] - accDp[l - 1]
    dp[i] %= MOD
    accDp[i] = (accDp[i - 1] + dp[i]) % MOD

print(dp[N])
