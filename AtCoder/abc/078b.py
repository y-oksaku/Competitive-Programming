X, Y, Z = map(int, input().split())
X -= 2 * Z

ans, r = divmod(X, Y + Z)
if r >= Y:
    ans += 1
print(ans)
