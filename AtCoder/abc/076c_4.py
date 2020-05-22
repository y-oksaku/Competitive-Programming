S = input()
T = input()

ans = []
for l in range(len(S) - len(T) + 1):
    U = S[l: l + len(T)]
    for u, t in zip(U, T):
        if u == '?':
            continue
        if u != t:
            break
    else:
        ans.append((S[:l] + T + S[l + len(T):]).replace('?', 'a'))

ans.sort()
print(ans[0] if len(ans) > 0 else 'UNRESTORABLE')
