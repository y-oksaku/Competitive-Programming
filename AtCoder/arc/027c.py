X, Y = map(int, input().split())
N = int(input())
TH = [tuple(map(int, input().split())) for _ in range(N)]
Z = X + Y

dp = [[0] * (Z + 1) for _ in range(N + 1)]
for t, h in TH:
    t -= 1
    for i in range(N)[::-1]:
        for z in range(Z):
            if i + 1 <= N and z + t <= Z and dp[i + 1][z + t] < dp[i][z] + h:
                dp[i + 1][z + t] = dp[i][z] + h

ans = 0
for k in range(1, min(X, N) + 1):
    ans = max(ans, dp[k][Z - k])
print(ans)
