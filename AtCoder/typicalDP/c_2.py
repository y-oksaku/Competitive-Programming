K = int(input())
N = 1 << K

R = [0] * N
for i in range(N):
    R[i] = int(input())

def pWinQ(p, q):
    return 1 / (1 + pow(10, (R[q] - R[p]) / 400))

dp = [[0] * (K + 1) for _ in range(N)]  # dp[person][round]
for i in range(N):
    dp[i][0] = 1

for k in range(1, K + 1):
    for i in range(N):
        enemy = i ^ (1 << (k - 1))
        for j in range(1 << (k - 1)):
            dp[i][k] += dp[i][k - 1] * dp[enemy ^ j][k - 1] * pWinQ(i, enemy ^ j)


for i in range(N):
    print('{:.16f}'.format(dp[i][K]))
