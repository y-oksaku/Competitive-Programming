from itertools import zip_longest
N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

def isSame(h, w):
    for lineA, lineB in zip_longest(A[h: h + M], B, fillvalue=[]):
        for a, b in zip_longest(lineA[w: w + M], lineB, fillvalue='?'):
            if a != b:
                return False
    return True

for h in range(N):
    for w in range(N):
        if isSame(h, w):
            print('Yes')
            exit()

print('No')