N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda a: a[0] + a[1], reverse=True)

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += AB[i][0]
    else:
        ans -= AB[i][1]
print(ans)
