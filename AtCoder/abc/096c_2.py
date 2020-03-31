H, W = map(int, input().split())
A = [input() for _ in range(H)]

def isOK():
    for h in range(H):
        for w in range(W):
            if A[h][w] == '.':
                continue
            if all([A[h + dh][w + dw] == '.' for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (0 <= h + dh < H and 0 <= w + dw < W)]):
                return False
    return True

print('Yes' if isOK() else 'No')
