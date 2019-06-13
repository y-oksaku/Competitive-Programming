import math

N , M = map(int,input().split())

if M == 0:
    a = [-1 , N+1]
else :
    a = [-1] * (M+2)

    for i in range(1,M+1) :
        a[i] = int(input())


flag = True # 可能かどうか
for i in range(0,M+1) :
    if a[i] + 1 == a[i+1] :
        flag = False
        break

fib = [1] * (N+1) # フィボナッチ数列
for i in range(2,N+1) :
    fib[i] = fib[i-1] + fib[i-2]

if flag :
    a[M+1] = N + 1

    ans = 1

    for i in range(M+1) :
        length = a[i+1] - a[i] - 2 # 上がる長さ
        ans *= fib[length]

    print(ans % 1000000007)
else :
    print(0)