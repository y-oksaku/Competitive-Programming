K, T = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(A)
ans = maxA - 1 - (K - maxA)
print(max(ans, 0))