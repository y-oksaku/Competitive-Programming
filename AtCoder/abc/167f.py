N = int(input())
S = [input() for _ in range(N)]

def calc(T):
    now = 0
    ret = 0
    for s in T:
        if s == '(':
            now += 1
        elif s == ')':
            now -= 1
        ret = min(ret, now)
    return ret

H = []
P = []
L = []

for s in S:
    less = -calc(s)
    if less == 0:
        H.append(s)
    else:
        l = s.count('(')
        r = len(s) - l
        if l >= r:
            P.append((less, s))
        else:
            L.append((less - (r - l), s))

P.sort(key=lambda a: a[0])
L.sort(key=lambda a: a[0], reverse=True)
P = [s for _, s in P]
L = [s for _, s in L]
ans = ''.join(H) + ''.join(P) + ''.join(L)

l = ans.count('(')
r = len(ans) - l

if l != r or calc(ans) < 0:
    print('No')
else:
    print('Yes')
