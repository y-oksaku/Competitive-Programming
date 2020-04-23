N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(M)]
LR.sort(key=lambda a: (a[0], -a[0]))

R = 10**18
ans = 0
for l, r in LR:
    if R <= l:
        ans += 1
        R = 10**18
    R = min(R, r)

print(ans + 1)
