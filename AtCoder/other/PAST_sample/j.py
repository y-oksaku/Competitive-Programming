N, M = map(int, input().split())
keys = []

for _ in range(M):
    cost, _ = map(int, input().split())
    mask = 0
    for c in map(int, input().split()):
        mask |= (1 << (c - 1))
    keys.append((cost, mask))

dp = [[float('inf')] * (1 << N) for _ in range(M + 1)]
dp[0][0] = 0

for i, (c, mask) in enumerate(keys, start=1):
    for state in range(1 << N):
        dp[i][state] = min(dp[i][state], dp[i - 1][state])
        dp[i][state | mask] = min(dp[i][state | mask], dp[i - 1][state] + c)

print('-1' if dp[M][(1 << N) - 1] == float('inf') else dp[M][(1 << N) - 1])