def sol():
    H, W = map(int, input().split())
    pic = [[1 for _ in range(W + 2)] for _ in range(H + 2)]

    picR = [[1 for _ in range(W + 4)] for _ in range(H + 4)]
    picC = [[1 for _ in range(H + 4)] for _ in range(W + 4)]
    for w in range(W + 4):
        picR[0][w] = 0
        picR[-1][w] = 0
        picC[w][0] = 0
        picC[w][-1] = 0
    for h in range(H + 4):
        picR[h][0] = 0
        picR[h][-1] = 0
        picC[0][h] = 0
        picC[-1][h] = 0

    for h in range(1, H + 1):
        line = input()
        for w in range(1, W + 1):
            if line[w - 1] == '#':
                pic[h][w] = 1
                picR[h + 1][w + 1] = 1
                picC[w + 1][h + 1] = 1
            else:
                pic[h][w] = 0
                picR[h + 1][w + 1] = 0
                picC[w + 1][h + 1] = 0

    for h in range(2, H + 2):
        for w in range(2, W + 2):
            if picR[h][w] == 1:
                if sum(picR[h][w - 2: w + 1]) == 3 or sum(picR[h][w - 1: w + 2]) == 3 or sum(picR[h][w: w + 3]) == 3:
                    continue
                else:
                    print('impossible')
                    return

            if picC[w][h] == 1:
                if sum(picR[w][h - 2: h + 1]) == 3 or sum(picR[w][h - 1: h + 2]) == 3 or sum(picR[w][h: h + 3]) == 3:
                    continue
                else:
                    print('impossible')
                    return

    def sumBlack(h, w):
        return pic[h - 1][w - 1] + pic[h - 1][w] + pic[h - 1][w + 1] + pic[h][w - 1] + pic[h][w] + pic[h][w + 1] + pic[h + 1][w - 1] + pic[h + 1][w] + pic[h + 1][w + 1]

    center = set([])
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if sumBlack(h, w) == 9:
                center.add((h, w))

    print('possible')
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if (h, w) in center:
                print('#', end='')
            else:
                print('.', end='')
        print('')

sol()