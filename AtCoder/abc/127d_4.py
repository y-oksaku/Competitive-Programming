from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = Counter(A)

for _ in range(M):
    b, c = map(int, input().split())
    cnt[c] += b

ans = 0
for b, c in sorted(cnt.items(), reverse=True):
    ans += min(c, N) * b
    N -= min(c, N)
    if N == 0:
        break
print(ans)