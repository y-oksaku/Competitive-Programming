N, M = map(int, input().split())
A = list(map(int, input().split()))

B = set([a & (-a) for a in A])
if len(B) > 1:
    print(0)
    exit()

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(x, y):
    return x * y // gcd(x, y)

A = [a // 2 for a in A]
LCM = A[0]
for a in A:
    LCM = lcm(LCM, a)

ans = ((M // LCM) + 1) // 2
print(ans)
