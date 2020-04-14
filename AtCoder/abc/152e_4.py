N = int(input())
MOD = 10**9 + 7
A = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(x, y):
    return x * y // gcd(x, y)

L = 1
for a in A:
    L = lcm(L, a)

L %= MOD
ans = 0
for a in A:
    ans += L * pow(a, MOD - 2, MOD)
print(ans % MOD)
