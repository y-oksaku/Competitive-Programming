from collections import Counter
M, N, K = map(int, input().split())
X = list(map(int, input().split()))
cntX = Counter(X)

ans = 1
for center in range(1, M + 1):
    cnt = cntX[center]
    for j in range(1, K + 1):
        if cntX[center - j] > 0 or cntX[center + j] > 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)