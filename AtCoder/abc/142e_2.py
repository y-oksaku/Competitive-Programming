N, M = map(int, input().split())
keys = []

for _ in range(M):
    cost, _ = map(int, input().split())
    mask = 0
    for i in map(int, input().split()):
        mask |= (1 << (i - 1))
    keys.append((cost, mask))

dp = [[float('inf')] * (1 << N) for _ in range(M + 1)]
dp[0][0] = 0

for i, (cost, mask) in enumerate(keys, start=1):
    for state in range(1 << N):
        dp[i][state] = min(dp[i - 1][state], dp[i][state])
        dp[i][state | mask] = min(dp[i - 1][state] + cost, dp[i][state | mask])

ans = dp[M][(1 << N) - 1]
if ans == float('inf'):
    print(-1)
else:
    print(ans)