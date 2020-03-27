S = input()

ans = [['?', 0]]
for s in S:
    if ans[-1][0] != s:
        ans.append([s, 0])
    ans[-1][1] += 1

T = ''
for s, c in ans[1:]:
    T += '{}{}'.format(s, c)
print(T)