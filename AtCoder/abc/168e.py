from collections import Counter
import sys
input = sys.stdin.buffer.readline

N = int(input())

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def make(a, b):
    if a == b == 0:
        return (0, 0, 0)
    if a == 0:
        return (0, 1, 0)
    if b == 0:
        return (1, 0, 0)

    s = 1 if a * b > 0 else -1
    a, b = abs(a), abs(b)

    g = gcd(a, b)
    a //= g
    b //= g

    return (a, b, s)

ABS = Counter([make(*map(int, input().split())) for _ in range(N)])

ans = 1
MOD = 10**9 + 7

for a, b, s in list(ABS.keys()):
    if a == b == 0:
        continue
    p = ABS[(a, b, s)]
    n = ABS[(b, a, -s)]

    ABS[(a, b, s)] = 0
    ABS[(b, a, -s)] = 0

    cnt = pow(2, p, MOD) + pow(2, n, MOD) - 1
    ans = (ans * cnt) % MOD

ans += ABS[(0, 0, 0)]

print((ans - 1) % MOD)
