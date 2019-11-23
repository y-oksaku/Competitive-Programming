N, T = map(int, input().split())
ans = float('inf')
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
print('TLE' if ans == float('inf') else ans)