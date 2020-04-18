from itertools import product
import string
S = input()
V = set(list(string.ascii_uppercase))

T = [[]]
for s in S:
    if s in V and len(T[-1]) > 0:
        T[-1].append(s)
        T.append([])
    else:
        T[-1].append(s)

S = [''.join(t) for t in T]
S.sort(key=lambda s: s.lower())
print(''.join(S))
