X, Y = map(int, input().split())

ans = 0
for i in [X, Y]:
    if i == 3:
        ans += 100000
    if i == 2:
        ans += 200000
    if i == 1:
        ans += 300000

if [1, 1] == [X, Y]:
    ans += 400000

print(ans)