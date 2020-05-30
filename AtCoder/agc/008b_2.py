N, K = map(int, input().split())
A = list(map(int, input().split()))

mx = sum(map(lambda a: max(a, 0), A))

M = sum(map(lambda a: max(a, 0), A[:K]))
S = sum(A[:K])

ans = mx - M + max(0, S)

for l, r in zip(A, A[K:]):
    M -= max(l, 0)
    M += max(r, 0)
    S -= l
    S += r

    ans = max(ans, mx - M + max(S, 0))

print(ans)
