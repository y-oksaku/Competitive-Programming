N, K = map(int, input().split())

if K == 1:
    print(N**3)
    exit()

ans = 0
for k in range(K):
    if (k * 2) % K != 0:
        continue
    M = (N // K) - (1 if k == 0 else 0)
    if N % K >= k:
        M += 1
    ans += M**3
print(ans)
