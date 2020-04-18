N, A, B, C, D = map(int, input().split())

def isOk():
    M = B - A
    R = D - C

    for k in range(N):
        Z = M - (N - 1 - 2 * k) * C
        if -R * k <= Z <= R * (N - 1 - k):
            return True
    return False

print('YES' if isOk() else 'NO')
