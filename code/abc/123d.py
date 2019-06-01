import numpy as np

x , y , z , k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

checked = np.zeros((x+1,y+1,z+1))

print(checked)

q = [(0 , 0 , 0 , A[0] + B[0] + C[0])]
checked[0][0][0] = 1
value = lambda X : X[3]

for _ in range(k) :
    now = q.pop()
    print(now[3])

    a = now[0]
    b = now[1]
    c = now[2]

    if a < x - 1 :
        if checked[a+1][b][c] == 0 :
            q.append((a+1 , b , c , A[a+1] + B[b] + C[c]))
            checked[a+1][b][c] = 1
    if b < y - 1 :
        if checked[a][b+1][c] == 0 :
            q.append((a , b+1 , c , A[a] + B[b+1] + C[c]))
            checked[a][b+1][c] = 1
    if c < z - 1 :
        if checked[a][b][c+1] == 0 :
            q.append((a , b , c+1 , A[a] + B[b] + C[c+1]))
            checked[a][b][c+1] = 1

    q.sort(key=value)