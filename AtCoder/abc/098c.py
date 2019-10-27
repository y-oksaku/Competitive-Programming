N = int(input())
S = input()

sumW = [0 for _ in range(N + 1)]
sumE = [0 for _ in range(N + 1)]

for i, s in enumerate(S) :
    sumW[i + 1] = sumW[i]
    sumE[i + 1] = sumE[i]
    if s == 'W' :
        sumW[i + 1] += 1
    else :
        sumE[i + 1] += 1

ans = float('inf')
for i, s in enumerate(S) :
    count = sumW[i] + (sumE[N] - sumE[i + 1])
    ans = min(ans, count)

print(ans)