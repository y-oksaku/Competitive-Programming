N = int(input())
A = [[]]

for _ in range(N):
    a = int(input())
    if len(A[-1]) > 0 and a < A[-1][-1]:
        A.append([])
    A[-1].append(a)

def isOk():
    for l, r in zip(A, A[1:]):
        if l[-1] + 1 < r[0]:
            return False
    for grp in A:
        for l, r in zip(grp, grp[1:]):
            if l + 1 < r:
                return False

    return A[0][0] == 0

if not isOk():
    print(-1)
    exit()

B = []
for a in A:
    B.extend(a)
B = [-10**18] + B[::-1]

ans = 0
for r, l in zip(B, B[1:]):
    if l >= r:
        ans += l
print(ans)
