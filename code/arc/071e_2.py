S = input()
T = input()
Q = int(input())

N = len(S)
M = len(T)
accSA = [0] * (N + 1)
accSB = [0] * (N + 1)
accTA = [0] * (M + 1)
accTB = [0] * (M + 1)

for i, s in enumerate(S, start=1):
    accSA[i] = accSA[i - 1]
    accSB[i] = accSB[i - 1]
    if s == 'A':
        accSA[i] += 1
    else:
        accSB[i] += 1

for i, t in enumerate(T, start=1):
    accTA[i] = accTA[i - 1]
    accTB[i] = accTB[i - 1]
    if t == 'A':
        accTA[i] += 1
    else:
        accTB[i] += 1

ans = []
for _ in range(Q):
    leftS, rightS, leftT, rightT = map(int, input().split())

    sA = accSA[rightS] - accSA[leftS - 1]
    sB = accSB[rightS] - accSB[leftS - 1]
    tA = accTA[rightT] - accTA[leftT - 1]
    tB = accTB[rightT] - accTB[leftT - 1]

    if (sA + sB * 2) % 3 == (tA + tB * 2) % 3:
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans, sep='\n')