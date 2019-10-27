N, K = map(int, input().split())
A = list(map(int, input().split()))

def gcd(n, m) :
    n, m = max(n, m), min(n, m)
    if m == 0 :
        return n
    return gcd(m, n % m)

dis = A[0]
for a in A :
    dis = gcd(dis, a)

for a in A :
    if a < K :
        continue
    if (a - K) % dis == 0 :
        print('POSSIBLE')
        break
else :
    print('IMPOSSIBLE')