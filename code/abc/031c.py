N = int(input())
A = list(map(int, input().split()))

ans = -float('inf')

for taka in range(N):
    aokiVal = -float('inf')
    takaVal = 0
    for aoki in range(N):
        takaSum = 0
        aokiSum = 0
        if aoki < taka:
            takaSum = sum(A[aoki: taka + 1: 2])
            aokiSum = sum(A[aoki + 1: taka + 1: 2])
        elif aoki == taka:
            continue
        else:
            takaSum = sum(A[taka: aoki + 1: 2])
            aokiSum = sum(A[taka + 1: aoki + 1: 2])

        if aokiVal < aokiSum:
            aokiVal = aokiSum
            takaVal = takaSum
    ans = max(ans, takaVal)

print(ans)