N, K = map(int, input().split())

M = N // K
ans = M * (M - 1) * (M - 2) + M * (M - 1) * 3 + M

if K % 2 == 0:
    if N % K >= K // 2:
        M += 1
    ans += M * (M - 1) * (M - 2) + M * (M - 1) * 3 + M

print(ans)
