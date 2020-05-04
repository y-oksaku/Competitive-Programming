N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

bigA = []
bigB = []
zero = []
for a, b in AB:
    if a > b:
        bigA.append((a, b))
    elif a < b:
        bigB.append((a, b))
    else:
        zero.append((a, b))

def calc():
    bigB.sort()
    bigA.sort(key=lambda a: (a[1], a[0]), reverse=True)

    X = 0
    ret = X
    for a, b in (bigB + zero + bigA):
        X += a
        ret = max(ret, X)
        X -= b

    return ret

print(calc())
