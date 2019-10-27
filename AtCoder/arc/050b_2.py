R, B = map(int, input().split())
x, y = map(int, input().split())

def isOk(n):
    a = (R - n) // (x - 1)
    b = (B - n) // (y - 1)

    if a < 0 or b < 0:
        return False

    if a + b >= n:
        return True
    else:
        return False

ok = 0
ng = R + B

while ng - ok > 1:
    mid = (ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)