N, K = map(int, input().split())
MOD = 10**9 + 7

def modInv(a, MOD=1000000007) :
    b = MOD
    u = 1
    v = 0
    while b :
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u
    u = u % MOD
    return u

base = K // N

if base == 0:
    ans = 1
    for i in range(1, N + K):
        ans *= i % MOD
    for i in range(1, K + 1):
        ans *= modInv(i) % MOD
    for i in range(1, N):
        ans *= modInv(i) % MOD
else:
    r = K % N
    ans = 1
    for i in range(1, N + 1):
        ans *= i % MOD
    for i in range(1, r + 1):
        ans *= modInv(i) % MOD
    for i in range(1, N - r + 1):
        ans *= modInv(i) % MOD

print(ans % MOD)
