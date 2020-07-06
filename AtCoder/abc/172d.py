N = int(input())

ans = 0
for d in range(1, N + 1):
    n = N // d
    ans += d * n * (n + 1) // 2
print(ans)
