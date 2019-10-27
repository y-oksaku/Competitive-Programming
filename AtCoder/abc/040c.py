N = int(input())
A = list(map(int, input().split())) + [0, 0]

dp = [float('inf') for _ in range(N + 2)]
dp[0] = 0
for i in range(N):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(A[i] - A[i + 1]))
    dp[i + 2] = min(dp[i + 2], dp[i] + abs(A[i] - A[i + 2]))

print(dp[N - 1])

