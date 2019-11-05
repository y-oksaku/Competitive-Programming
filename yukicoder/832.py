from collections import Counter
from itertools import product

S = list(map(int, list(input())))
cntS = Counter(S)
ans = set()

def isOk(B):
    B.sort()
    cntB = Counter(B)
    for i in range(1, 10):
        while cntB[i] > 0:
            for j in range(i, i + 3):
                if cntB[j] == 0:
                    return False
                cntB[j] -= 1
    if all(c == 0 for c in cntB.values()):
        return True
    return False

for add in range(1, 10):
    if cntS[add] == 4:
        continue

    T = S + [add]
    cntT = Counter(T)

    if all(c == 2 for c in cntT.values()):
        ans.add(add)
        continue

    for (h1, h2) in product(range(14), repeat=2):
        if h1 == h2 or T[h1] != T[h2]:
            continue

        A = [t for i, t in enumerate(T) if i != h1 and i != h2]
        cntA = Counter(A)
        for mask in range(1 << 10):
            for d in range(1, 10):
                if (mask & (1 << (d - 1))) > 0:
                    if cntA[d] < 3:
                        break
            else:
                B = []
                for s, c in cntA.items():
                    if (mask & (1 << (s - 1))) > 0:
                        B += [s] * (c - 3)
                    else:
                        B += [s] * c

                if isOk(B):
                    ans.add(add)
                    break

ans = list(ans)
ans.sort()
for a in ans:
    if cntS[a] <= 3:
        print(a)