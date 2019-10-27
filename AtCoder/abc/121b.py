import numpy as np

N , M , C = map(int,input().split())
B = np.array(list(map(int,input().split())))
A = [0] * N

for i in range(N) :
    A[i] = list(map(int,input().split()))

A = np.array(A)
AB = A.dot(B)

ans = 0

for i in range(N) :
    if AB[i] + C > 0 :
        ans += 1

print(ans)