N = int(input())
XYC = [tuple(map(int, input().split())) for _ in range(N)]

def isOk(R, A):
    left = -10**18
    right = 10**18
    for x, c in A:
        left = max(left, x - R / c)
        right = min(right, x + R / c)
    return left <= right

ngX = 0
okX = 10**10
A = [(x, c) for x, _, c in XYC]
for _ in range(100):
    mid = (ngX + okX) / 2
    if isOk(mid, A):
        okX = mid
    else:
        ngX = mid

ngY = 0
okY = 10**10
A = [(y, c) for _, y, c in XYC]
for _ in range(100):
    mid = (ngY + okY) / 2
    if isOk(mid, A):
        okY = mid
    else:
        ngY = mid

print(max(okX, okY))
