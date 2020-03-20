N = int(input())
P = list(map(lambda a: int(a) - 1, input().split()))

ans = 0
for i in range(N):
    p = P[i]
    if p == i:
        if i < N - 1:
            P[i], P[i + 1] = P[i + 1], P[i]
        ans += 1

print(ans)