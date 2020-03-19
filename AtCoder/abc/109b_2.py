N = int(input())
A = [input() for _ in range(N)]

def isOk():
    if len(set(A)) < N:
        return False

    for a, b in zip(A, A[1:]):
        if a[-1] != b[0]:
            return False
    return True

print('Yes' if isOk() else 'No')
