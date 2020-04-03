A, B, C, X, Y = map(int, input().split())

ans = 10**18
for ab in range(max(X, Y) * 2 + 10):
    a = max(0, X - ab // 2)
    b = max(0, Y - ab // 2)
    ans = min(ans, A * a + B * b + C * ab)
print(ans)
