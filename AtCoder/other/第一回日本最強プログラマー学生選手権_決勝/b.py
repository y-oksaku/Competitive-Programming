N = int(input())

xToY = [[] for _ in range(N)]

for x in range(N):
    A = input()
    for y, a in enumerate(A):
        if a == '1':
            xToY[x].append(y)

xToZ = [[] for _ in range(N)]
noYToZ = [set([]) for _ in range(N)]

for x in range(N):
    B = input()
    for z, b in enumerate(B):
        if b == '1':
            xToZ[x].append(z)
        else:
            for y in xToY[x]:
                noYToZ[y].add(z)

yToz = [set([]) for _ in range(N)]
for x in range(N):
    for z in xToZ[x]:
        for y in xToY[x]:
            if z in noYToZ[y]:
                continue
            yToz[y].add(z)
            break
        else:
            print(-1)
            exit()

for y in range(N):
    ans = []
    for z in range(N):
        if z in yToz[y]:
            ans.append('1')
        else:
            ans.append('0')
    print(''.join(ans))