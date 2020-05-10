A, B, C, K = map(int, input().split())

ans = 0
a = min(A, K)
ans += a

K -= a
b = min(B, K)
K -= b

c = min(C, K)
ans -= c

print(ans)
