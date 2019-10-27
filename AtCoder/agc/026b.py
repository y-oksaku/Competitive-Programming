T = int(input())

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

ans = []
for _ in range(T):
    A, B, C, D = map(int, input().split())

    if A < B:
        ans.append('No')
        continue

    if B > D:
        ans.append('No')
        continue

    if C >= B:
        ans.append('Yes')
        continue

    # A >= B, B <= D, C < B
    G = gcd(D, B)
    maxMod = B - G + A % G
    if C < maxMod:
        ans.append('No')
    else:
        ans.append('Yes')

print(*ans, sep='\n')