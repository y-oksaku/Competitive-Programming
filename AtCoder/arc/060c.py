N, A = map(int, input().split())
X = list(map(int, input().split()))
Y = [x - A for x in X]

dp = [[0 for _ in range(20000)] for _ in range(N + 1)]

def bias(n):
    return n + 5000

dp[0][bias(0)] = 1

for i in range(N):
    for s in range(-5000, 5000):
        dp[i + 1][bias(s)] += dp[i][bias(s)]
        dp[i + 1][bias(s + Y[i])] += dp[i][bias(s)]

print(dp[N][bias(0)] - 1)