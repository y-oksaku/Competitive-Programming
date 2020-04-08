N, K = map(int, input().split())

if K == 0:
    print(N**2)
    exit()

ans = 0
for d in range(K + 1, N + 1):
    ans += (N // d) * (d - K)
    ans += max(0, N % d - K + 1)
print(ans)