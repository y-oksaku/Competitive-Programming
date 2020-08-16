X, K, D = map(int, input().split())
X = abs(X)

k = min(K, X // D)
X -= k * D
K -= k

print(X if K % 2 == 0 else abs(X - D))
