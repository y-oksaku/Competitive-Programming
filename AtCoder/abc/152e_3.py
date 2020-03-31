N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(n, m):
    return n * m // gcd(n, m)

LCM = 1
for a in A:
    LCM = lcm(LCM, a)

LCM %= MOD
ans = 0
for a in A:
    ans += LCM * pow(a, MOD - 2, MOD)
print(ans % MOD)
