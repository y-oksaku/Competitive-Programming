import math

A , B = map(int,input().split())

bA = bin(A)
bB = bin(B)


if (A - 1) % 2 == 0 :
    fA = A - 1
    fA += ((A - 1) / 2) % 2
else :
    fA = (A / 2) % 2

if B % 2 == 0 :
    fB = B
    fB += (B / 2) % 2
else :
    fB = ((B + 1) / 2) % 2

bfA = bin(int(fA))
bfB = bin(int(fB))

bAB = [0] * (max(len(bfA) , len(bfB)) - 2)
ans = 0

for i in range(1,len(bAB) + 1) :
    if i > len(bfA) - 2 :
        bAB[-i] = int(bfB[-i])
    elif i > len(bfB) - 2 :
        bAB[-i] = int(bfA[-i])
    else :
        bAB[-i] = 1 if (int(bfA[-i]) + int(bfB[-i])) % 2 == 1 else 0

for b in bAB : # デコード
    ans = ans * 2 + b

print(ans)
