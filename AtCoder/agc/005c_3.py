from collections import Counter

N = int(input())
A = list(map(int, input().split()))

def canMake():
    if N == 2:
        return A == [1, 1]

    cntA = Counter(A)
    mi = min(A)
    mx = max(A)

    if mi < mx // 2:
        return False

    if mx % 2 == 0 and cntA[mi] > 1:
        return False
    if mx % 2 == 1 and cntA[mi] > 2:
        return False

    for i in range(mi + 1, mx + 1):
        if cntA[i] < 2:
            return False

    return True

print('Possible' if canMake() else 'Impossible')
