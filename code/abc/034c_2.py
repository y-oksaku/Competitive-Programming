H, W = map(int, input().split())
fact = [1 for _ in range(H + W + 100)]
MOD = 10**9 + 7

for i in range(1, H + W + 100):
    fact[i] = fact[i - 1] * i % MOD

# MODにおける逆元
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

ans = (fact[H + W - 2] * modInv(fact[H - 1]) % MOD) * modInv(fact[W - 1]) % MOD
print(ans)