N, Q = map(int, input().split())
ans = [0] * N
for _ in range(Q):
    l, r, t = map(int, input().split())
    for i in range(l - 1, r):
        ans[i] = t
print(*ans, sep='\n')
