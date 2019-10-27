N = int(input())
A = list(map(int,input().split()))

minus = 1
for i,a in enumerate(A) :
    if a < 0 :
        minus *= -1
        A[i] = -a

ans = sum(A)

A.sort()

if minus == -1 :
    ans -= A[0] * 2

print(ans)
