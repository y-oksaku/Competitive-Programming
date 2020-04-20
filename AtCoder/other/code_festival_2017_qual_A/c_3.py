from collections import Counter
H, W = map(int, input().split())
cntA = Counter()

for _ in range(H):
    cntA += Counter(list(input()))

four = (H // 2) * (W // 2)
for a, c in cntA.items():
    if four <= 0:
        break
    while c >= 4 and four > 0:
        c -= 4
        four -= 1
    cntA[a] = c

if four > 0:
    print('No')
    exit()

if H % 2 == W % 2 == 1:
    for a, c in cntA.items():
        if c % 2 == 1:
            cntA[a] -= 1
            break
    else:
        print('No')
        exit()

print('Yes' if all(c % 2 == 0 for c in cntA.values()) else 'No')
