N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def dist(x, y, u, v):
    return ((x - u)**2 + (y - v)**2)**0.5

ans = 0
for i, (x, y) in enumerate(XY):
    for u, v in XY[i + 1:]:
        ans += dist(x, y, u, v)

print(2 * ans / N)