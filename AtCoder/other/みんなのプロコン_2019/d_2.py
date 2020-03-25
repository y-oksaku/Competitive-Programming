L = int(input())
A = [int(input()) for _ in range(L)]

def cost(k, a):
    if k == 0 or k == 4:
        return a

    if a % 2:
        a = 1
    elif a >= 2:
        a = 2

    if k == 1 or k == 3:
        return 2 - a

    return 1 - a % 2

dp = [[10**18] * 5 for _ in range(L + 1)]
dp[0][0] = 0

for i, a in enumerate(A, start=1):
    for j in range(5):
        for k in range(j, 5):
            b = dp[i - 1][j] + cost(k, a)
            if dp[i][k] > b:
                dp[i][k] = b

ans = min(dp[L])
print(ans)