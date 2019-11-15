S = input()
C = len(S)
F = 0
for i, s in enumerate(S):
    if s == 'C':
        C = min(i, C)
    if s == 'F':
        F = max(i, F)

if C < F:
    print('Yes')
else:
    print('No')