MOD = 1000000007

L = input().strip()
length = len(L)

dp1 = [-1] * length
dp2 = [-1] * length

# L[0] = 1
dp1[0] = 1  # a, b = 0, 0
dp2[0] = 2  # a, b = 1, 0 or 0, 1

for i in range(1, length) :
    dp1[i] = dp1[i - 1] * 3 % MOD  # いずれのa,bでもL以下のまま

    if L[i] == '1' :
        dp1[i] += dp2[i - 1] % MOD  # a, b = 0, 0 のとき確定
        dp2[i] = (dp2[i - 1] * 2) % MOD  # a, b = 1, 0 or 0, 1 のときまだ不明
    else :
        dp2[i] = dp2[i - 1]

print((dp1[-1] + dp2[-1]) % MOD)