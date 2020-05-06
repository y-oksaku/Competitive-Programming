N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    if i >= K:
        ans += 1
    else:
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += pow(2, -cnt)
print(ans / N)
