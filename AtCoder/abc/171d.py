from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

S = sum(A)
cntA = Counter(A)

for _ in range(Q):
    B, C = map(int, input().split())
    D = C - B
    S += D * cntA[B]
    cntA[C] += cntA[B]
    cntA[B] = 0

    print(S)