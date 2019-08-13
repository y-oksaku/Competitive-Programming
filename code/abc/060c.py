N, T = map(int, input().split())
time = list(map(int, input().split()))
time.append(float('inf'))

ans = 0
for i in range(N):
    ans += min(T, time[i + 1] - time[i])

print(ans)