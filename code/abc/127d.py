N , M = map(int,input().split())

A = list(map(int,input().split()))

A.sort()

conv = []

for i in range(M) :
    B , C = map(int,input().split())
    conv.append([B,C])

sec = lambda A : A[1]
conv.sort(key=sec,reverse=True)

change = []
add = 0

# 大きいものからN個とる
for c in conv :
    for i in range(c[0]) :
        change.append(c[1])
        add += 1

    if(add >= N) :
        break

for i in range(min(N,len(change))) :
    if A[i] >= change[i] :
        break
    A[i] = change[i]

print(int(sum(A)))