W = int(input())
N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
M = 50 * 100 + 100

dp = [[10**10] * M for _ in range(K + 1)]
dp[0][0] = 0

for a, b in AB:
    for k in range(K)[:: -1]:
        for m in range(M):
            if m + b < M:
                dp[k + 1][m + b] = min(dp[k + 1][m + b], dp[k][m] + a)

ans = 0
for d in dp:
    for m in range(M):
        if d[m] <= W:
            ans = max(ans, m)

print(ans)