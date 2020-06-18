W, H, N = map(int, input().split())
XYA = [tuple(map(int, input().split())) for _ in range(N)]

def isBlack(h, w):
    for x, y, a in XYA:
        if a == 1 and w < x:
            return True
        if a == 2 and w >= x:
            return True
        if a == 3 and h < y:
            return True
        if a == 4 and h >= y:
            return True
    return False

ans = H * W
for w in range(W):
    for h in range(H):
        ans -= 1 if isBlack(h, w) else 0
print(ans)
