N, M = map(int, input().split())
LRS = [tuple(map(int, input().split())) for _ in range(N)]

accL = [0] * (M + 2)
accR = [0] * (M + 2)

for l, r, s in LRS:
    accL[r] += s
    accR[l] += s

for i in range(1, M + 2):
    accL[i] += accL[i - 1]
    accR[-(i + 1)] += accR[-i]

ans = 0
for mid in range(1, M + 1):
    ans = max(ans, accL[mid - 1] + accR[mid + 1])
print(ans)
