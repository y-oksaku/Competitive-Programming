S = input()
T = input()

def canMake(left):
    for s, t in zip(S[left:], T):
        if s == '?':
            continue
        if s != t:
            return False
    return True

ans = []
for left in range(len(S) - len(T) + 1):
    if canMake(left):
        Z = S[: left] + T + S[left + len(T):]
        ans.append(Z.replace('?', 'a'))

if len(ans) == 0:
    ans.append('UNRESTORABLE')
ans.sort()
print(ans[0])