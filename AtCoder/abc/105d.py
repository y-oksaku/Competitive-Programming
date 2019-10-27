N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(N) :
    S[i+1] = S[i] + A[i]

cat = {}
for s in S :
    mod = s % M
    if mod in cat :
        cat[mod] += 1
    else :
        cat[mod] = 1

def comb(n, k) :
    p = 1
    d = 1
    for i in range(k) :
        p *= (n - i)
        d *=(i + 1)
    return p // d

ans = 0
for key, val in cat.items() :
    if val < 2 :
        continue
    ans += comb(val, 2)

print(ans)
