H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0 :
    print('0')
else :
    ans = min(W, H)
    for a1 in [W // 3, -(-W // 3)] :
        for a2 in [H // 2, -(-H // 2)] :
            A1 = a1 * H
            A2 = a2 * (W - a1)
            A3 = H * W - A1 - A2
            ans = min(ans, max(A1, A2, A3) - min(A1, A2, A3))
    for a1 in [H // 3, -(-H // 3)] :
        for a2 in [W // 2, -(-W // 2)] :
            A1 = a1 * W
            A2 = a2 * (H - a1)
            A3 = H * W - A1 - A2
            ans = min(ans, max(A1, A2, A3) - min(A1, A2, A3))
    print(ans)