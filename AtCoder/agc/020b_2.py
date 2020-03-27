K = int(input())
A = list(map(int, input().split()))

mx = 2
mi = 2

for a in A[:: -1]:
    mx = (-(-(mx + 1) // a)) * a - 1
    mi = (-(-mi // a)) * a

def isOk(x):
    for a in A:
        x = (x // a) * a
    return x == 2

if isOk(mi) and isOk(mx):
    print(mi, mx)
else:
    print(-1)
