N, X = map(int, input().split())
A = [X] + list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

B = [abs(a - A[0]) for a in A]
ans = 0
for d in B:
    ans = gcd(ans, d)
print(ans)
