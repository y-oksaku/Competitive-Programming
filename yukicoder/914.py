N, M, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * (K + 1) for _ in range(N + 1)]
dp[0][K] = True

for i, item in enumerate(items, start=1):
    for price in item:
        for k in range(K + 1):
            if k + price <= K:
                dp[i][k] |= dp[i - 1][k + price]

ans = -1
for p, a in enumerate(dp[N]):
    if a:
        ans = p
        break

print(ans)