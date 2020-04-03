from collections import Counter
H, W = map(int, input().split())
cntA = Counter()
for _ in range(H):
    cntA += Counter(list(input()))

if H % 2 + W % 2 == 0:
    if all(c % 4 == 0 for c in cntA.values()):
        print('Yes')
    else:
        print('No')
    exit()

if H % 2 + W % 2 == 1:
    two = (H if H % 2 == 0 else W) // 2
    cntTwo = 0
    for c in cntA.values():
        if c % 4 == 0:
            continue
        if c % 2 == 0:
            cntTwo += 1
            continue
        break
    else:
        if cntTwo <= two:
            print('Yes')
            exit()
    print('No')
    exit()

cntTwo = 0
cntOdd = 0
for c in cntA.values():
    if c % 4 == 0:
        continue
    if c % 2 == 0:
        cntTwo += 1
        continue
    cntOdd += 1

if cntOdd == 1 and cntTwo <= (H + W - 2) // 2:
    print('Yes')
    exit()

print('No')