N, X, Y, Z = map(int, input().split())
MOD = 10**9 + 7

# X-Y-Zを含まない数列を数える
D = 2**(X + Y + Z - 1)  # 直前のX+Y+Zビットを保持する

# ビットが立っている部分で数列を区切れる
XYZ = (1 << (X + Y + Z - 1)) | (1 << (Y + Z - 1)) | (1 << (Z - 1))  # X-Y-Z

dp = [[0] * D for _ in range(N + 1)]
dp[0][0] = 1

for right in range(N):
    for mask in range(D):
        for nextA in range(1, 11):
            # 110 + 10 = 110 10
            newMask = (mask << (nextA)) | (1 << (nextA - 1))
            if newMask & XYZ != XYZ:  # X-Y-Zを含まない
                dp[right + 1][newMask % D] += dp[right][mask]
                dp[right + 1][newMask % D] %= MOD

ans = pow(10, N, MOD) - sum(dp[-1])
print(ans % MOD)