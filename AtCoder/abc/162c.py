N = int(input())

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            ans += gcd(i, gcd(j, k))
print(ans)
