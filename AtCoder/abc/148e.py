N = int(input())

if N % 2 == 1:
    print(0)
else:
    ans = 0
    while N > 0:
        ans += N // 10
        N //= 5
    print(ans)
