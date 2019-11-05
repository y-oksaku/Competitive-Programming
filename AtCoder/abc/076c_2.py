S = input()
T = input()
ans = []

for left in range(len(S)):
    subS = S[left: left + len(T)]
    if len(subS) < len(T):
        break
    for s, t in zip(subS, T):
        if s == '?':
            continue
        if s != t:
            break
    else:
        U = S[:left] + T + S[left + len(T):]
        ans.append(U.replace('?', 'a'))

if len(ans) == 0:
    print('UNRESTORABLE')
else:
    ans.sort()
    print(ans[0])