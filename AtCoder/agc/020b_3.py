K = int(input())
A = list(map(int, input().split()))

def g(x):
    for a in A:
        x = (x // a) * a
    return x

overEq = 10**18
less = 0
while overEq - less > 1:
    mid = (overEq + less) // 2
    if g(mid) < 2:
        less = mid
    else:
        overEq = mid

over = 10**18
lessEq = 0
while over - lessEq > 1:
    mid = (over + lessEq) // 2
    if g(mid) <= 2:
        lessEq = mid
    else:
        over = mid

if g(overEq) == 2 and g(lessEq) == 2:
    print(overEq, lessEq)
else:
    print(-1)
