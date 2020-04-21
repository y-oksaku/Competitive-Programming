N, K = map(int, input().split())

if K == 0:
    print(N**2)
    exit()

ans = 0
for b in range(K + 1, N + 1):
    q, r = divmod(N, b)
    ans += q * (b - K)
    ans += max(0, r - K + 1)
print(ans)
