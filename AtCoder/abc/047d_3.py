N, _ = map(int, input().split())
A = list(map(int, input().split()))

mi = 10**18
mx = -10**18
ans = 0
for a in A:
    if mx < a - mi:
        ans = 0
        mx = a - mi
    if mx == a - mi:
        ans += 1
    mi = min(mi, a)

print(ans)
