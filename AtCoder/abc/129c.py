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

fact = [0] * (N+2)

if flag :
    a[M+1] = N + 1

    ans = 1

    for i in range(M+1) :
        length = a[i+1] - a[i] - 2 # 上がる長さ
        max2step = math.floor(length / 2) # 2段の回数
        count = 1
        for j in range(1,max2step+1) :
            if fact[j] != 0 :
                step2 = fact[j]
            else :
                step2 = math.factorial(j)
                fact[j] = step2
            if fact[length-2*j] != 0 :
                step1 = fact[length-2*j]
            else :
                step1 = math.factorial(length-2*j)
                fact[length-2*j] = step1
            if fact[length - j] != 0 :
                step3 = fact[length-j]
            else :
                step3 = math.factorial(length - j)
                fact[length - j] = step3
            count += step3 // step1 // step2
        ans *= count

    print(ans % 1000000007)
else :
    print(0)