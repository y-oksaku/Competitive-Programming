N = int(input())

ans = (N // 11) * 2
res = N % 11

if res == 0:
    pass
elif res == 1 or res == 3 or res == 4 or res == 6 or res == 2 or res == 5:
    ans += 1
else:
    ans += 2

print(ans)