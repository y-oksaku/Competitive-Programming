N = int(input())

ans = int(input())

def gcd(n, m):
    n, m = max(n, m), min(n, m)
    if m == 0:
        return n
    return gcd(m, n % m)


for _ in range(N - 1):
    t = int(input())
    ans = (ans * t) // gcd(ans, t)

print(ans)