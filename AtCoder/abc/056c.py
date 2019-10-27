X = int(input())

ans = X
for n in range(1, X):
    if n * (n + 1) >= 2 * X:
        ans = min(ans, n)
        break

print(ans)