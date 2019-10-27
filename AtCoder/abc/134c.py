N = int(input())
A = []

for i in range(N) :
    a = int(input())
    A.append((a, i))

A.sort(key=lambda A : A[0], reverse=True)

for i in range(N) :
    if i == A[0][1] :
        print(A[1][0])
    else :
        print(A[0][0])
