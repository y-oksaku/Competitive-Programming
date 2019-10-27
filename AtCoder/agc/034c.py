import math

N , X = map(int,input().split())

B = [0] * N

minPointB = 0 # 最小得点

for i in range(N) :
    b , l , u = map(int,input().split())
    B[i] = (i,b,l,u)
    minPointB += b * l

dom = lambda B : B[3] * (X - B[1]) / X # 追いつける速度

B.sort(key=dom,reverse=True)

ans = 0

for i in range(N) :
    if minPointB <= B[i][3] * (X - B[i][1]) : # 追いつけた場合
        for j in range(B[i][1]+1,X+1) :
            if minPointB <= B[i][3] * (j - B[i][1]) :
                ans += j
                break
        break
    else :
        minPointB -= B[i][3] * (X - B[i][1])
        ans += X

print(int(ans))