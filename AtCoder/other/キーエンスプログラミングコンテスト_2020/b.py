N = int(input())
XL = [tuple(map(int, input().split())) for _ in range(N)]

XL.sort(key=lambda a: (a[0] + a[1], a[0] - a[1]))

ans = 0
R = -10**18
for x, l in XL:
    if R <= x - l:
        ans += 1
        R = x + l
print(ans)
