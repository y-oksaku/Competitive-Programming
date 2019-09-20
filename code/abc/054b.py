N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

if N == M:
    if A == B:
        print('Yes')
    else:
        print('No')
    exit()

def isEmbeded(left, top):
    subA = [a[left: left + M] for a in A[top: top + M]]
    if subA == B:
        return True
    else:
        return False

for left in range(N - M):
    for top in range(N - M):
        if isEmbeded(left, top):
            print('Yes')
            exit()

print('No')