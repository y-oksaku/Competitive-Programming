N = int(input())

dp = [float('inf') for _ in range(N + 1)]
dp[N] = 0

for i in range(N, -1, -1) :
    if i - 1 >= 0 :
        dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    dis = 6
    while i - dis >= 0 :
        dp[i - dis] = min(dp[i - dis], dp[i] + 1)
        dis *= 6
    dis = 9
    while i - dis >= 0 :
        dp[i - dis] = min(dp[i - dis], dp[i] + 1)
        dis *= 9

print(dp[0])