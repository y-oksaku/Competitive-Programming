H, A, D = map(int, input().split())

ans = -(-H // A)
for normal in range(H + 1):
    magic = H - normal
    ans = min(ans, -(-normal // A) + -(-magic // D) * (3 / 2))

print(ans)
