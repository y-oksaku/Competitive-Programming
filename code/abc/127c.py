N , M = map(int,input().split())

Lmax = 0
Rmin = 10**5 + 1

for i in range(M) :
    L , R = map(int,input().split())

    Lmax = max(Lmax,L)
    Rmin = min(Rmin,R)


if Lmax <= Rmin :
    print(int(Rmin - Lmax + 1))
else :
    print(0)