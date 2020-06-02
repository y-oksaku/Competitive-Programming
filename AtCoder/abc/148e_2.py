N = int(input())

if N % 2 == 1:
    print(0)
    exit()

ans = 0
while N > 0:
    N //= 10
    ans += N
    for i in range(1, 100):
        ans += -(-(N // pow(5, i)) // 2)
print(ans)
