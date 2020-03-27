R, C, K = map(int, input().split())
A = [tuple(map(lambda a: a == 'x', input())) for _ in range(R)]

accA = []
for r, B in enumerate(A):
    S = [0] * (C + 1)
    for c in range(1, C + 1):
        S[c] = S[c - 1] + B[c - 1]
    accA.append(S)

def hasBlack(r, c, k):
    S = accA[r]
    return S[c + k] - S[c - (k + 1)] > 0

ans = 0
for r in range(K - 1, R - K + 1):
    for c in range(K - 1, C - K + 1):
        isOk = True
        for k, i in enumerate(range(r - (K - 1), r)):
            if hasBlack(i, c + 1, k):
                isOk = False
                break
        if not isOk:
            continue
        for k, i in enumerate(range(r, r + K)[:: -1]):
            if hasBlack(i, c + 1, k):
                isOk= False
                break
        if not isOk:
            continue

        ans += 1

print(ans)
