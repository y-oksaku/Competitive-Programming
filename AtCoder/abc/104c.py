D, G = map(int, input().split())

problems = [tuple(map(int, input().split())) for _ in range(D)]
ans = 10**10

for mask in range(1 << D):
    point = 0
    cnt = 0
    for i, (p, c) in enumerate(problems):
        if (mask & (1 << i)) > 0:
            cnt += p
            point += 100 * (i + 1) * p + c

    if point >= G:
        ans = min(ans, cnt)
        continue

    for i, (p, c) in enumerate(problems):
        if (mask & (1 << i)) > 0:
            continue
        ness = -(-(G - point) // (100 * (i + 1)))
        if ness <= p:
            ans = min(ans, cnt + ness)

print(ans)
