N = int(input())
T = [int(input()) for _ in range(N)]
T.sort()

ans = 10**18
for mask in range(1 << N):
    A, B = 0, 0
    for i, t in enumerate(T):
        if (mask & (1 << i)) > 0:
            A += t
        else:
            B += t
    ans = min(ans, max(A, B))
print(ans)
