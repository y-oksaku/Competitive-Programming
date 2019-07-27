S = input()
MOD = 10**9 + 7
lenS = len(S)

dp = [[0 for _ in range(13)] for _ in range(lenS + 1)]  # dp[digit][d] = digit桁までの mod=d の数
dp[0][0] = 1

digitMask = 1

for digit in range(1, lenS + 1) :
    if(S[-digit] == '?') :
        for d in range(13) :
            for k in range(10) :
                dp[digit][d] = (dp[digit][d] + dp[digit - 1][(d - k * digitMask) % 13]) % MOD
    else :
        a = int(S[-digit])
        for d in range(13) :
            dp[digit][d] = (dp[digit][d] + dp[digit - 1][(d - a * digitMask) % 13]) % MOD
    digitMask *= 10

ans = (dp[len(S)][5]) % MOD
print(ans)

