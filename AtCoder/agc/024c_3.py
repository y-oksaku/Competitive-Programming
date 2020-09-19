import sys
input = sys.stdin.buffer.readline

N = int(input())
G = [[]]
A = []

for _ in range(N):
    a = int(input())
    if len(G[-1]) > 0 and G[-1][-1] > a:
        G.append([])
    A.append(a)
    G[-1].append(a)

def isOk():
    if any(l[-1] + 1 < r[0] for l, r in zip(G, G[1:])):
        return False
    for grp in G:
        if any(l + 1 < r for l, r in zip(grp, grp[1:])):
            return False
    return A[0] == 0

if not isOk():
    print(-1)
    exit()

ans = 0
A = [-10**18] + A[::-1]

for r, l in zip(A, A[1:]):
    if l >= r:
        ans += l
print(ans)
