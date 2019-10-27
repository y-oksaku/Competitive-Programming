N, M = map(int, input().split())

imsLeft = [0 for _ in range(M + 2)]
imsRight = [0 for _ in range(M + 2)]
sumScore = 0
for _ in range(N):
    l, r, s = map(int, input().split())
    imsLeft[l] -= s
    imsRight[r + 1] += s
    sumScore += s

imsLeft[0] = sumScore
for i in range(1, M + 2):
    imsLeft[i] += imsLeft[i - 1]
    imsRight[i] += imsRight[i - 1]

ans = 0
for mid in range(1, M + 1):
    score = imsLeft[mid] + imsRight[mid]
    ans = max(ans, score)

print(ans)