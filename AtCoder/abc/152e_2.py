N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(n, m):
    return n * m // gcd(n, m)

L = A[0]
for a in A:
    L = lcm(L, a)
L %= MOD

modInvSum = sum([pow(a, MOD - 2, MOD) for a in A])
ans = L * modInvSum

print(ans % MOD)
