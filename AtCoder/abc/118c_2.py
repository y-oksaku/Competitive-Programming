N = int(input())
A = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

G = A[0]
for a in A:
    G = gcd(G, a)

print(G)
