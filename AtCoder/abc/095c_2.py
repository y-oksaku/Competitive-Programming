A, B, C, X, Y = map(int, input().split())

ans = 10**10
for ab in range(max(X, Y) * 2 + 10):
    price = C * ab + max(0, X - ab // 2) * A + max(0, Y - ab // 2) * B
    ans = min(ans, price)

print(ans)
