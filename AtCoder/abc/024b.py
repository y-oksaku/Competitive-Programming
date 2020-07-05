N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
t = 0
for a in A:
    ans += a + T - max(a, t)
    t = a + T
print(ans)
