H, W = map(int, input().split())

if H == 1 and W == 1 :
    print(0)
else :
    coins = [[0 for _ in range(W)] for _ in range(H)]
    minCoin = [-1, -1, 10]

    for h in range(H) :
        A = list(map(int, input().split()))
        for w in range(W) :
            coins[h][w] = A[w]
            if A[w] < minCoin[2] :
                minCoin = [h, w, A[w]]

    ans = []

    # 最小のコインに奇数を集める
    for h in range(0, minCoin[0]) :
        for w in range(W) :
            if coins[h][w] % 2 == 1 :
                coins[h + 1][w] += 1
                ans.append([h, w, h+1, w])

    for h in range(H-1, minCoin[0], -1) :
        for w in range(W) :
            if coins[h][w] % 2 == 1 :
                coins[h - 1][w] += 1
                ans.append([h, w, h-1, w])

    for w in range(0, minCoin[1]) :
        if coins[minCoin[0]][w] % 2 == 1 :
            coins[minCoin[0]][w + 1] += 1
            ans.append([minCoin[0], w, minCoin[0], w+1])

    for w in range(W-1, minCoin[1], -1) :
        if coins[minCoin[0]][w] % 2 == 1 :
            coins[minCoin[0]][w - 1] += 1
            ans.append([minCoin[0], w, minCoin[0], w-1])

    if coins[minCoin[0]][minCoin[1]] % 2 == 1 :  # 奇数が余った場合
        lastMoves = []
        if minCoin[0] > 0 :
            lastMoves.append([minCoin[0]-1, minCoin[1], coins[minCoin[0]-1][minCoin[1]]])
        if minCoin[0] < H - 1 :
            lastMoves.append([minCoin[0]+1, minCoin[1], coins[minCoin[0]+1][minCoin[1]]])
        if minCoin[1] > 0 :
            lastMoves.append([minCoin[0], minCoin[1]-1, coins[minCoin[0]][minCoin[1]-1]])
        if minCoin[1] < W - 1 :
            lastMoves.append([minCoin[0], minCoin[0]+1, coins[minCoin[0]][minCoin[1]+1]])
        lastMoves.sort(key=lambda A : A[2])
        toCoin = lastMoves[0]
        if toCoin[2] < coins[minCoin[0]][minCoin[1]] - 1 :
            ans.append([minCoin[0], minCoin[1]] + toCoin[0:2])

    print(len(ans))
    for a in ans :
        print(a[0]+1, a[1]+1, a[2]+1, a[3]+1)