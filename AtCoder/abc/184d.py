A, B, C = map(int, input().split())

dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
dp[A][B][C] = 1

for a in range(A, 100):
    for b in range(B, 100):
        for c in range(C, 100):
            S = a + b + c
            now = dp[a][b][c]
            dp[a + 1][b][c] += a / S * now
            dp[a][b + 1][c] += b / S * now
            dp[a][b][c + 1] += c / S * now

ans = 0
for i in range(100):
    for j in range(100):
        ans += (dp[100][i][j] + dp[i][100][j] + dp[i][j][100]) * (100 + i + j - A - B - C)
print(ans)
