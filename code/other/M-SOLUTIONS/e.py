q = int(input())

ans = [0] * q

for i in range(q) :
    x , d , n = map(int,input().split())
    ans[i] = x
    for j in range(1,n) :
        ans[i] *= (x + j*d)
    ans[i] = ans[i] % 1000003

for a in ans :
    print(a)
