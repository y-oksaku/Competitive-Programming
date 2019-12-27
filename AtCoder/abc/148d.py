N = int(input())
A = list(map(int, input().split()))

ans = 0
now = 1
for a in A:
    if a == now:
        now += 1
    else:
        ans += 1

if now == 1:
    print(-1)
else:
    print(ans)