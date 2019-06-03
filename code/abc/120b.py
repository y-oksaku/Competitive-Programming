import math

A , B , K = map(int,input().split()) # A,B <= 100

k = 0

R = int(max(math.gcd(A,B),1))

for i in range(R,0,-1) :
    if A % i == 0 and B % i == 0 :
        k += 1
        if k >= K :
            print(i)
            break

