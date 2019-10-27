N = int(input())

point = []
dist = []
maxDist = 0

for _ in range(N) :
    x, y = map(int, input().split())
    d = abs(x) + abs(y)
    maxDist = max(maxDist, d)
    point.append((x, y, d))
    dist.append(d)

mask = maxDist % 2

for d in dist :
    if d % 2 != mask :  # 実現不可能
        print('-1')
        break
else :  # 実現可能
    print(maxDist) # 腕の数
    tmp = (5 * 10**4)
    out = [1] * tmp
    for _ in range(maxDist // tmp) :
        print(*out)
    out = [1] * (maxDist % tmp)
    print(*out)

    for x, y, d in point :
        if x < 0 :
            for _ in range(-x) :
                print('L', end='')
        elif x > 0 :
            for _ in range(x) :
                print('R', end='')

        if y < 0 :
            for _ in range(-y) :
                print('D', end='')
        elif y > 0 :
            for _ in range(y) :
                print('U', end='')

        R = (maxDist - d) // 2
        if R > 0 :
            for _ in range(R) :
                print('LR', end='')

        print('')
