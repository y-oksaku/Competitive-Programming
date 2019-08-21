def gcd(a,b) :
    r = a % b
    if r == 0 :
        return b
    else :
        return gcd(b,r)

N = int(input())

A = list(map(int,input().split()))

L = [0] * N
R = [0] * N

for i in range(N) :  # iより左(右)
    if i == 0 :
        L[i] = A[i]
        R[-i-1] = A[-i-1]
        R[-i-1] = A[-i-1]
        R[-i-1] = A[-i-1]
    else :
        L[i] = gcd(L[i-1], A[i-1])
        R[-i-1] = gcd(R[-i],A[-i])

ans = 1

for i in range(N) :
    if i == 0 :
        new = R[i]
    elif i == N-1 :
        new = L[i]
    else :
        new = gcd(L[i],R[i])
    if ans < new :
        ans = new

print(ans)
