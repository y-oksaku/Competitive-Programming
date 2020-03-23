from collections import defaultdict

N, P = map(int, input().split())
S = input()

def solMin():
    dp = [[0] * P for _ in range(N + 1)]

    for i, s in enumerate(map(int, S), start=1):
        dp[i][s % P] += 1
        for p in range(P):
            dp[i][(p * 10 + s) % P] += dp[i - 1][p]

    return sum(dp[i][0] for i in range(N + 1))

def solLarge():
    cnt = defaultdict(int)
    ret = 0
    now = 0

    for d, s in enumerate(map(int, S[:: -1])):
        now += pow(10, d, P) * s
        now %= P
        ret += cnt[(now - P) % P]
        if now == 0:
            ret += 1
        cnt[now] += 1

    return ret

print(solMin() if P * N <= 10**6 else solLarge())
