H = int(input())
ans = 0
now = 1
while H > 0:
    ans += now
    now *= 2
    H //= 2

print(ans)