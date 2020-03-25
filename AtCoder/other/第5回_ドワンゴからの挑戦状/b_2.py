N, K = map(int, input().split())
A = list(map(int, input().split()))

S = []
for i in range(N):
    s = 0
    for a in A[i:]:
        s += a
        S.append(s)

def isOk(n):
    return sum([n & a == n for a in S]) >= K

ans = 0
for d in range(40)[:: -1]:
    if isOk(ans | (1 << d)):
        ans |= (1 << d)

print(ans)
