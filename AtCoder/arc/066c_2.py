from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cntA = Counter(A)

if len(A) % 2 == 1:
    if cntA[0] != 1:
        print(0)
        exit()
    cnt = 1
    for i in range(2, N, 2):
        if cntA[i] != 2:
            print(0)
            exit()
        cnt += 2
    if cnt != N:
        print(0)
        exit()
else:
    cnt = 0
    for i in range(1, N, 2):
        if cntA[i] != 2:
            print(0)
            exit()
        cnt += 2
    if cnt != N:
        print(0)
        exit()

print(pow(2, N // 2, 10**9 + 7))
