S = input()

grp = []
prev = '?'
for s in S:
    if s == prev:
        grp[-1].append(s)
    else:
        grp.append([s])
    prev = s

ans = ''
for g in grp:
    ans += g[0] + str(len(g))
print(ans)
