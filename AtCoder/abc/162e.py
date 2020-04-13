N, K = map(int, input().split())
MOD = 10**9 + 7

cnt = [0] * (K + 1)

def calc(x):
    M = K // x
    c = pow(M, N, MOD)
    for i in range(x + x, K + 1, x):
        c -= cnt[i]
    cnt[x] = c
    return c * x

ans = 0
for x in range(1, K + 1)[::-1]:
    ans = (ans + calc(x)) % MOD
print(ans)
