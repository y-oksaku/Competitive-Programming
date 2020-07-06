H, W, K = map(int, input().split())
A = [input() for _ in range(H)]

ans = 0
for row in range(1 << H):
    R = set([i for i in range(H) if (row & (1 << i)) != 0])
    for col in range(1 << W):
        C = set([i for i in range(W) if (col & (1 << i)) != 0])

        cnt = 0
        for h in range(H):
            for w in range(W):
                if A[h][w] == '.' or h in R or w in C:
                    continue
                cnt += 1

        if cnt == K:
            ans += 1

print(ans)
