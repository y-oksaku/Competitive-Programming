N, S, T = map(int, input().split())

W = 0
ans = 0

for _ in range(N):
    W += int(input())
    ans += 1 if S <= W <= T else 0

print(ans)