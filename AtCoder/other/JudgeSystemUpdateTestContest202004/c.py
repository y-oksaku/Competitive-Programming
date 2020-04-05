from itertools import permutations
A, B, C = map(int, input().split())
N = A + B + C

def isOk(X, Y, Z):
    for Q in (X, Y, Z):
        if Q != tuple(sorted(Q)):
            return False
    for fr, to in ((X, Y), (Y, Z)):
        for i, j in zip(fr, to):
            if i >= j:
                return False
    return True

ans = 0
for P in permutations(range(1, N + 1), r=N):
    X = P[:A]
    Y = P[A: A + B]
    Z = P[A + B:]

    ans += 1 if isOk(X, Y, Z) else 0

print(ans)
