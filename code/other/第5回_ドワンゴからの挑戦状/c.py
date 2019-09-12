N, K = map(int, input().split())
A = list(map(int, input().split()))

cumA = [0] * (N + 1)
for i in range(1, N + 1):
    cumA[i] = cumA[i - 1] + A[i - 1]

beauty = []
for left in range(N):
    for right in range(left + 1, N + 1):
        b = cumA[right] - cumA[left]
        beauty.append(b)

ans = 0
M = max(beauty).bit_length()

for digit in range(M)[:: -1]:
    new = ans + (1 << digit)
    cnt = 0
    for b in beauty:
        if b & new == new:
            cnt += 1
    if cnt >= K:
        ans = new

print(ans)