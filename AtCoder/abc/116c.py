N = int(input())
H = list(map(int, input().split()))
ans = 0

while max(H) > 0:
    grp = [[]]
    for i, h in enumerate(H):
        if h == 0:
            if len(grp[-1]) > 0:
                grp.append([])
        else:
            grp[-1].append((i, h))
    for g in grp:
        if len(g) == 0:
            continue
        mi = min([h for _, h in g])
        ans += mi
        for i, _ in g:
            H[i] -= mi

print(ans)
