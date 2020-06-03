N, A, B = map(int, input().split())
X = list(map(int, input().split()))
D = [r - l for l, r in zip(X, X[1:])]

ans = sum(min(A * d, B) for d in D)
print(ans)
