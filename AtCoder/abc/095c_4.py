A, B, C, X, Y = map(int, input().split())

ans = 10**18
for c in range(max(X, Y) * 2 + 1):
    x = max(0, X - c // 2)
    y = max(0, Y - c // 2)
    ans = min(ans, x * A + y * B + c * C)
print(ans)
