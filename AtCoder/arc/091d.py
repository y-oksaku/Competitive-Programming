N, K = map(int, input().split())

if K == 0:
    print(N**2)
    exit()

ans = 0
for div in range(K + 1, N + 1):
    cnt = N // div
    ans += cnt * (div - K)
    ans += max(0, (N % div) - K + 1)

print(ans)