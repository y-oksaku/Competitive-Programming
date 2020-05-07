N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]

AB.sort(key=lambda a: (a[1], a[0]))

mx = 10**18
ans = 0
for a, b in AB:
    if a >= mx:
        ans += 1
        mx = 10**18
    mx = min(mx, b)
print(ans + 1)
