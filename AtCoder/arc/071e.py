S = input()
T = input()

cumSA = [0] * (len(S) + 1)
cumSB = [0] * (len(S) + 1)
cumTA = [0] * (len(T) + 1)
cumTB = [0] * (len(T) + 1)

for i, s in enumerate(S, start=1):
    cumSA[i] = cumSA[i - 1]
    cumSB[i] = cumSB[i - 1]

    if s == 'A':
        cumSA[i] += 1
    else:
        cumSB[i] += 1

for i, t in enumerate(T, start=1):
    cumTA[i] = cumTA[i - 1]
    cumTB[i] = cumTB[i - 1]

    if t == 'A':
        cumTA[i] += 1
    else:
        cumTB[i] += 1

Q = int(input())
ans = []
for _ in range(Q):
    lS, rS, lT, rT = map(int, input().split())

    sA = cumSA[rS] - cumSA[lS - 1]
    sB = cumSB[rS] - cumSB[lS - 1]
    tA = cumTA[rT] - cumTA[lT - 1]
    tB = cumTB[rT] - cumTB[lT - 1]

    if (sA - sB) % 3 == (tA - tB) % 3:
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans, sep='\n')

