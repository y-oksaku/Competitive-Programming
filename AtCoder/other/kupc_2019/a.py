N, X = map(int, input().split())
A = list(map(int, input().split()))

maxA = max(A)
ans = sum([a + X >= maxA for a in A])

print(ans)