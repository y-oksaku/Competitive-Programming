N = int(input())

R = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

R.sort(reverse=True)

ans  = 0
used = set([-1])

for x, y in R:
    take = -1
    for i, (u, v) in enumerate(B):
        if x < u and y < v and (not i in used):
            if take == -1:
                take = i
            else:
                if v < B[take][1]:
                    take = i
    if not take in used:
        ans += 1
        used.add(take)

print(ans)