X = int(input())
now = 100
ans = 0

while now < X:
    now += now // 100
    ans += 1

print(ans)

