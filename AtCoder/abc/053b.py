S = input()
l = len(S)
r = -1

for i, s in enumerate(S):
    if s == 'A':
        l = min(l, i)
    if s == 'Z':
        r = max(r, i)

print(r - l + 1)
