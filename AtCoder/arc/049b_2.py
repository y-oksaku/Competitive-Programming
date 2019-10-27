N = int(input())
EPS = 1e-8

point = []

for _ in range(N):
    x, y, c = map(int, input().split())
    point.append((x, y, c))

ng = 0
ok = 10**7

def isOkX(cx):
    left = 0
    right = 0
    for x, _, c in point:
        if x >= cx:
            right = max(right, c * abs(cx - x))
        else:
            left = max(left, c * abs(cx - x))
    return left < right

ok = -10**6
ng = 10**6
while abs(ng - ok) > EPS:
    mid = (ng + ok) / 2
    if isOkX(mid):
        ok = mid
    else:
        ng = mid

cX = ok

def isOkY(cy):
    left = 0
    right = 0
    for _, y, c in point:
        if y >= cy:
            right = max(right, c * abs(cy - y))
        else:
            left = max(left, c * abs(cy - y))
    return left < right

ok = -10**6
ng = 10**6
while abs(ng - ok) > EPS:
    mid = (ng + ok) / 2
    if isOkY(mid):
        ok = mid
    else:
        ng = mid

cY = ok

ans = 0
for x, y, c in point:
    ans = max(ans, c * max(abs(x - cX), abs(y - cY)))

print(ans)