N, M = map(int, input().split())

parts = []
for _ in range(M):
    mask = 0
    s, c = input().split()
    for i, f in enumerate(s):
        if f == 'Y':
            mask |= (1 << i)
    parts.append((mask, int(c)))

INF = 10**18
dp = [INF] * (1 << N)
dp[0] = 0
for state in range(1 << N):
    for mask, c in parts:
        if dp[state | mask] > dp[state] + c:
            dp[state | mask] = dp[state] + c

ans = dp[(1 << N) - 1]
print(ans if ans < INF else -1)
