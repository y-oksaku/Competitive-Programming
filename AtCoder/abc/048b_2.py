A, B, X = map(int, input().split())
ans = max(0, B // X - (A - 1) // X)
print(ans)