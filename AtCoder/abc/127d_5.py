from collections import Counter
N, M = map(int, input().split())
cnt = Counter(map(int, input().split()))

for _ in range(M):
    B, C = map(int, input().split())
    cnt[C] += B

ans = 0
for n, c in sorted(cnt.items(), reverse=True):
    if N == 0:
        break
    mi = min(c, N)
    ans += mi * n
    N -= mi
print(ans)
