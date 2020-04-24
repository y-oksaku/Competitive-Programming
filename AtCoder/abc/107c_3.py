N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10**18
for l, r in zip(X, X[K - 1:]):
    if r <= 0:
        ans = min(ans, abs(l))
    if l >= 0:
        ans = min(ans, abs(r))
    if l < 0 < r:
        ans = min(ans, r - l + min(abs(r), abs(l)))
print(ans)
