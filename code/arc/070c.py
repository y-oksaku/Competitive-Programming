X = int(input())

ans = 1
while ans * (ans + 1) // 2 < X:
    ans += 1

print(ans)