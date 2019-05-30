import math

N = int(input())
A = list(map(int,input().split()))

ans = 1

if N == 1 :
    ans = A[0]
else :
    for i in range(N) :
        B = A[:i-1] + A[i:] # i番目を除く
        stat = B[0]
        for b in B[1:] :
            stat = math.gcd(stat,b)
            if stat == 1:
                break
        else :
            ans = max(ans,stat)

print(ans)
