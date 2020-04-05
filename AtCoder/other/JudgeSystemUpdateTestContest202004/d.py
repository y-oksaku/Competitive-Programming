N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = list(map(int, input().split()))

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

G = [0] * (N + 1)
for i, a in enumerate(A, start=1):
    G[i] = gcd(G[i - 1], a)

def search(x):
    if gcd(G[-1], x) != 1:
        return gcd(G[-1], x)

    ng = 0
    ok = N
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if gcd(G[mid], x) == 1:
            ok = mid
        else:
            ng = mid
    return ok

ans = []
for s in S:
    ans.append(search(s))
print(*ans, sep='\n')

