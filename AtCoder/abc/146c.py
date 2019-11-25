A, B, X = map(int, input().split())

ok = 0
ng = X

while ng - ok > 1:
    mid = (ng + ok) // 2
    if mid * A + len(str(mid)) * B <= X and mid <= 10**9:
        ok = mid
    else:
        ng = mid

print(ok)