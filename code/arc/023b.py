R, C, D = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(R)]

ans = 0
for r, row in enumerate(A):
    for w, a in enumerate(row):
        if (r + w) <= D and (r + w) % 2 == D % 2:
            ans = max(ans, a)

print(ans)