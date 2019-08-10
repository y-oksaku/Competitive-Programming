N, X = map(int, input().split())
axis = list(map(int, input().split()))

ans = abs(axis[0] - X)

def gcd(n, m) :
    n, m = max(n, m), min(n, m)
    if m == 0 :
        return n
    return gcd(m, n % m)

for a in axis :
    ans = gcd(ans, abs(a - X))

print(ans)