N = int(input())
XYH = [tuple(map(int, input().split())) for _ in range(N)]
bx, by, bh = [xyh for xyh in XYH if xyh[2] > 0][0]

def solve(cx, cy):
    H = abs(cx - bx) + abs(cy - by) + bh

    for x, y, h in XYH:
        D = max(0, H - abs(cx - x) - abs(cy - y))
        if D != h:
            return 0
    return H

for x in range(101):
    for y in range(101):
        h = solve(x, y)
        if h > 0:
            print(x, y, h)
            exit()

print(-1)
