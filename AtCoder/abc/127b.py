r , D , x0 = map(int,input().split())

xk = x0

for i in range(10) :
    xk = r * xk - D
    print(int(xk))