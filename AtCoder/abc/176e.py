H, W, M = map(int, input().split())
bomb = [tuple(map(lambda a: int(a) - 1, input().split())) for _ in range(M)]

cntRow = [0] * H
cntCol = [0] * W
for h, w in bomb:
    cntRow[h] += 1
    cntCol[w] += 1

mxR = max(cntRow)
mxC = max(cntCol)

R = set([h for h in range(H) if cntRow[h] == mxR])
C = set([w for w in range(W) if cntCol[w] == mxC])

ans = mxR + mxC
if len([0 for h, w in bomb if h in R and w in C]) == len(R) * len(C):
    ans -= 1

print(ans)
