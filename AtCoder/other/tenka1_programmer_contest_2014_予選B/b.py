N = int(input())
S = input()
T = [input() for _ in range(N)]
M = len(S)
MOD = 10**9 + 7

dp = [0] * (M + 1)
dp[0] = 1

for l in range(M):
    for t in T:
        r = l + len(t)
        if r > M:
            continue
        if S[l: r] == t:
            dp[r] = (dp[r] + dp[l]) % MOD

print(dp[-1])
