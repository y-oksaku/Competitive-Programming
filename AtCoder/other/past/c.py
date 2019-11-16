N, T = map(int, input().split())
ans = float('inf')
for _ in range(N):
    cost, time = map(int, input().split())
    if time <= T:
        ans = min(ans, cost)

print('TLE' if ans == float('inf') else ans)