N = int(input())
S = input()

L = S.count('(')
R = S.count(')')

if L > R:
    S = S + (')' * (L - R))
if R > L:
    S = ('(' * (R - L)) + S

d = 0
mx = 0
for s in S:
    if s == ')':
        d += 1
    else:
        d -= 1
    mx = max(mx, d)

S = '(' * mx + S + ')' * mx
print(S)
