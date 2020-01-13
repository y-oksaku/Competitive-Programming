from math import sin

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def dist(x, y, u, v):
    return ((x - u)**2 + (y - v)**2)**0.5

ans = 10**10

for i in range(N):
    for j in range(i + 1, N):
        # 対辺
        xi, yi = XY[i]
        xj, yj = XY[j]
        cx = (xi + xj) / 2
        cy = (yi + yj) / 2
        d = 0
        for x, y in XY:
            d = max(d, dist(x, y, cx, cy))
        ans = min(ans, d)

        for k in range(j + 1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            xk, yk = XY[k]
            c = dist(xi, yi, xj, yj)
            a = dist(xj, yj, xk, yk)
            b = dist(xk, yk, xi, yi)

            # 外心
            S = a**2 * (b**2 + c**2 - a**2) + b**2 * (c**2 + a**2 - b**2) + c**2 * (a**2 + b**2 - c**2)
            if S == 0:
                continue
            cx = a**2 * (b**2 + c**2 - a**2) * xi + b**2 * (c**2 + a**2 - b**2) * xj + c**2 * (a**2 + b**2 - c**2) * xk
            cy = a**2 * (b**2 + c**2 - a**2) * yi + b**2 * (c**2 + a**2 - b**2) * yj + c**2 * (a**2 + b**2 - c**2) * yk
            cx /= S
            cy /= S
            d = 0
            for x, y in XY:
                d = max(d, dist(x, y, cx, cy))
            ans = min(ans, d)

print(ans)
