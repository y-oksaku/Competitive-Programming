H, W = map(int, input().split())

A = [input() for _ in range(H)]

confilm = [[False] * W for _ in range(H)]
confilm[0][0] = True

nH, nW = 0, 0
while True:
    isMoved = False
    while nW < W - 1 and A[nH][nW + 1] == '#':
        nW += 1
        confilm[nH][nW] = True
        isMoved = True
    while nH < H - 1 and A[nH + 1][nW] == '#':
        nH += 1
        confilm[nH][nW] = True
        isMoved = True

    if not isMoved:
        break

for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            if confilm[h][w]:
                continue
            else:
                print('Impossible')
                exit()
        else:
            if confilm[h][w]:
                print('Impossible')
                exit()
            else:
                continue

print('Possible')


