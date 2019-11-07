N, K = map(int, input().split())
A = list(map(int, input().split()))
M = int(max(max(A), K)).bit_length()

maxVal = [0] * M  # digit以下の桁で取れる最大値

for digit in range(M):
    cnt = 0
    mask = (1 << digit)
    for a in A:
        if (mask & a) > 0:
            cnt += 1
    cnt = max(cnt, N - cnt)
    maxVal[digit] = cnt * mask
    if digit > 0:
        maxVal[digit] += maxVal[digit - 1]

upperValK = [0] * (M + 1)

for digit in range(M)[:: -1]:
    mask = (1 << digit)
    maskedK = (K & mask)
    cnt = 0
    for a in A:
        if (a & mask) != maskedK:
            cnt += mask
    upperValK[digit] = cnt + upperValK[digit + 1]

ans = upperValK[0]
for mid in range(M):
    mask = (1 << mid)
    if not (mask & K) > 0:
        continue

    cnt = upperValK[mid + 1]
    for a in A:
        if (a & mask) > 0:
            cnt += mask
    if mid > 0:
        cnt += maxVal[mid - 1]
    ans = max(ans, cnt)

print(ans)