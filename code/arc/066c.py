from collections import Counter

N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

cntA = Counter(A)

if N % 2 == 0:
    for i in range(1, N, 2):
        if cntA[i] != 2:
            print(0)
            exit()
        cntA[i] = 0
    if max(cntA.values()) > 0:
        print(0)
        exit()
    print(pow(2, N // 2, MOD))
else:
    for i in range(2, N, 2):
        if cntA[i] != 2:
            print(0)
            exit()
        cntA[i] = 0
    if cntA[0] != 1:
        print(0)
        exit()
    cntA[0] = 0
    if max(cntA.values()) > 0:
        print(0)
        exit()
    print(pow(2, N // 2, MOD))