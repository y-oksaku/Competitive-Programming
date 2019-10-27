B = list(input().split())

numToIndex = {n : i for i, n in enumerate(B)}

N = int(input())
A = [input() for _ in range(N)]

def isLess(X, Y):
    if len(X) < len(Y):
        return True
    elif len(X) > len(Y):
        return False
    else:
        for x, y in zip(X, Y):
            if numToIndex[x] < numToIndex[y]:
                return True
            elif numToIndex[x] > numToIndex[y]:
                return False
        return False

for left in range(N):
    minIndex = left
    for i in range(left + 1, N):
        if isLess(A[i], A[minIndex]):
            minIndex = i
    A[left], A[minIndex] = A[minIndex], A[left]

print(*A, sep='\n')
