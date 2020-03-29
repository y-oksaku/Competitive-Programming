S = input()

now = 0
ans = 0
for s in S:
    if now == 0:
        now += 1
        if s == 'p':
            ans -= 1
        continue
    if s == 'g':
        ans += 1
    now -= 1

print(ans)
