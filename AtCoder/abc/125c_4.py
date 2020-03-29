N = int(input())
A = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

L = [0] * (N + 1)
R = [0] * (N + 1)

for i, a in enumerate(A, start=1):
    L[i] = gcd(L[i - 1], a)
for i, a in enumerate(A[:: -1], start=1):
    R[i] = gcd(R[i - 1], a)

R = R[:: -1]
ans = 1
for mid in range(1, N + 1):
    ans = max(ans, gcd(L[mid - 1], R[mid]))
print(ans)
