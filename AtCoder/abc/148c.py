A, B = map(int, input().split())

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

ans = A * B // gcd(A, B)
print(ans)