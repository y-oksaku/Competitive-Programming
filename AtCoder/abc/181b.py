N = int(input())
S = lambda n: n * (n + 1) // 2

ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += S(b) - S(a - 1)
print(ans)
