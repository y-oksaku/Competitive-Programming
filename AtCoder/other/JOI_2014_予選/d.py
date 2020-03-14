N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [10**10] * (N + 1)
dp[0] = 0

for c in C:
    for i in range(N)[:: -1]:
        dp[i + 1] = min(dp[i + 1], dp[i] + c * D[i])

print(dp[N])
