N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(M)]
AB.sort(key=lambda a: (a[0], -a[1]))

ans = 1
right = 10**18
for l, r in AB:
    if l >= right:
        ans += 1
        right = 10**18
    right = min(right, r)
print(ans)