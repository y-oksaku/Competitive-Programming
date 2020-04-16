N = int(input())
S = input()

l = S.count('(')
r = S.count(')')
d = r - l

if d > 0:
    S = '(' * d + S
if d < 0:
    S = S + ')' * (-d)

l, r, d = 0, 0, 0
for s in S:
    if s == '(':
        l += 1
    if s == ')':
        r += 1
    d = max(d, r - l)

if d > 0:
    S = '(' * d + S + ')' * d

print(S)
