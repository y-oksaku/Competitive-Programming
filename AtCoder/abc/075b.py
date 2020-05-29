from itertools import product

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
D = tuple(product((-1, 0, 1), repeat=2))

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        cnt = 0
        for dh, dw in D:
            if 0 <= h + dh < H and 0 <= w + dw < W and S[h + dh][w + dw] == '#':
                cnt += 1
        S[h][w] = str(cnt)

for s in S:
    print(''.join(s))
