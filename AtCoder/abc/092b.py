N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X
for a in A:
    now = 1
    while now <= D:
        ans += 1
        now += a
print(ans)
