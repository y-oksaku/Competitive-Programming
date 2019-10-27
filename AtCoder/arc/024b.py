N = int(input())
C = [int(input()) for _ in range(N)]

if len(set(C)) == 1:
    print('-1')
    exit()

C = C + C

maxLeng = 1
leng = 1
for i in range(2 * N - 1):
    if C[i] == C[i + 1]:
        leng += 1
    else:
        leng = 1
    maxLeng = max(maxLeng, leng)

if maxLeng % 2 == 0:
    print(maxLeng // 2)
else:
    print(maxLeng // 2 + 1)