N = int(input())

ans = 0
for _ in range(N - 1):
    fr, to = map(int, input().split())
    if fr > to:
        fr, to = to, fr
    ans += fr * (N - to + 1)

for l in range(1, N + 1):
    ans -= (N * (N + 1) // 2 - l * (l - 1) // 2)
    ans += (l - 1) * (N - l + 1)
print(-ans)
