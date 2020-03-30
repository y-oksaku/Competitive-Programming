x, y = map(int, input().split())
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def distLine(a, b, c):
    return abs(a * x + b * y + c) / ((a**2 + b**2)**0.5)

def dist(u, v):
    return ((x - u)**2 + (y - v)**2)**0.5

ans = 10**18
for (u1, v1), (u2, v2) in zip(XY, XY[1:] + [XY[0]]):
    ans = min(ans, dist(u1, v1))
    if u2 == u1:
        ans = min(ans, abs(x - u1))
        continue

    a = (v2 - v1) / (u2 - u1)
    b = v1 - a * u1
    ans = min(ans, distLine(a, -1, b))

print(ans)