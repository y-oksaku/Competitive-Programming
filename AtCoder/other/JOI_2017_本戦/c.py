N = int(input())
XY = [tuple(map(float, input().split())) for _ in range(N)]
S = set(XY)

def rot(x, y, u, v):
    mx = (x + u) / 2
    my = (y + v) / 2
    x, y = -(y - my), x - mx
    return (x + mx, y + my), (-x + mx, -y + my)

ans = 0
for i, (x, y) in enumerate(XY):
    for u, v in XY[i + 1:]:
        # 対角線で考える
        if all(V in S for V in rot(x, y, u, v)):
            area = ((x - u)**2 + (y - v)**2) / 2
            ans = max(ans, area)

print(int(ans))
