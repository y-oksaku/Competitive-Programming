from copy import deepcopy
N, A, B = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(N)]
R = 500

dp = [[10**18] * R for _ in range(R)]
dp[0][0] = 0

for a, b, c in ABC:
    newDp = deepcopy(dp)
    for x in range(R):
        for y in range(R):
            if x + a < R and y + b < R:
                newDp[x + a][y + b] = min(newDp[x + a][y + b], dp[x][y] + c)
    dp = newDp

ans = 10**18
for x in range(1, R):
    for y in range(1, R):
        if B * x == A * y:
            ans = min(ans, dp[x][y])
print(ans if ans < 10**18 else -1)
