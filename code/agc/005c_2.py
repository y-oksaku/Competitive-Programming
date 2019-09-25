from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cntA = Counter(A)
valA= list(set(A))
valA.sort()

if valA[-1] % 2 == 1:
    if valA[0] != -(-valA[-1] // 2) or cntA[valA[0]] != 2:
        print('Impossible')
        exit()

    for a in range(valA[0], valA[-1] + 1):
        if cntA[a] < 2:
            print('Impossible')
            exit()
else:
    if valA[0] != valA[-1] // 2 or cntA[valA[0]] != 1:
        print('Impossible')
        exit()

    for a in range(valA[0] + 1, valA[-1] + 1):
        if cntA[a] < 2:
            print('Impossible')
            exit()

print('Possible')
