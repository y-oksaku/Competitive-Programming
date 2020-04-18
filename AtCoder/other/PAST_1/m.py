N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(M)]

def canMake(S):
    XY = AB + [min(CD, key=lambda a: S * a[0] - a[1])]
    XY.sort(key=lambda a: S * a[0] - a[1])

    mass, magic = 0, 0
    for a, b in XY[:5]:
        mass += a
        magic += b

    return S <= magic / mass

ok = 0
ng = 10**6

for _ in range(100):
    mid = (ok + ng) / 2
    if canMake(mid):
        ok = mid
    else:
        ng = mid
print(ok)
