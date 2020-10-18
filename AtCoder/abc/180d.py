X, Y, A, B = map(int, input().split())

ans = 0
for a in range(Y + 10):
    prd = X * pow(A, a)
    if prd >= Y:
        break
    b = max(0, (Y - prd - 1) // B)
    ans = max(ans, a + b)
print(ans)
