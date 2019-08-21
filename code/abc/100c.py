N = int(input())

ans = 0
for a in map(int, input().split()) :
    while a % 2 == 0 :
        ans += 1
        a //= 2

print(ans)