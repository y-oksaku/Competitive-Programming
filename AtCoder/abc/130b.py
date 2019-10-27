import math

N , X = map(int,input().split())
L = list(map(int,input().split()))

now = 0
ans = 1
for i in range(N) :
    now += L[i]
    if now <= X :
        ans += 1
    else :
        break

print(ans)