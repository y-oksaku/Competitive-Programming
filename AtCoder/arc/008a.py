N = int(input())

ans = (N // 10) * 100
N %= 10

if N >= 7:
    ans += 100
else:
    ans += N * 15

print(ans)