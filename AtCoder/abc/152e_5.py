N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(a, b):
    return a * b // gcd(a, b)

L = 1
for a in A:
    L = lcm(L, a)

L %= MOD
coef = 0
for a in A:
    coef += pow(a, MOD - 2, MOD)
print((L * coef) % MOD)
