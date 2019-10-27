N, A = map(int, input().split())
X = list(map(int, input().split()))

Y = [x - A for x in X]

dp = [[0] * 10000 for _ in range(N + 1)]
dp[0][5000] = 1

for m in range(1, N + 1):
    for s in range(-5000, 5001):
        if s + 5000 < 10000:
            dp[m][s + 5000] += dp[m - 1][s + 5000]
            if 0 <= s - Y[m - 1] + 5000 < 10000:
                dp[m][s + 5000] += dp[m - 1][s - Y[m - 1] + 5000]

print(dp[N][5000] - 1)