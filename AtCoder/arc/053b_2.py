from collections import Counter
S = input()

cntS = Counter(list(S))

two = 0
one = 0
for c in cntS.values():
    q, r = divmod(c, 2)
    two += q
    one += r

if one == 0:
    print(len(S))
else:
    print(two // one * 2 + 1)
