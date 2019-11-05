N = int(input())
Y = list(map(int, input().split()))
Y.sort()

if N <= 3:
    print(Y[-1] - Y[0])
    exit()

INF = float('inf')
dp = [0] * (N + 1)
dp[0] = 0
dp[1] = INF
dp[2] = Y[1] - Y[0]
dp[3] = Y[2] - Y[0]

for i in range(4, N + 1):
    d1 = dp[i - 2] + Y[i - 1] - Y[i - 2]  # xxx o o
    d2 = dp[i - 3] + Y[i - 1] - Y[i - 3]  # xxx o o o
    d3 = dp[i - 4] + Y[i - 1] - Y[i - 2] + Y[i - 3] - Y[i - 4]  # xxx o o o o
    dp[i] = min(d1, d2, d3)

print(dp[N])