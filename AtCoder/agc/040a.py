S = input()
N = len(S)

A = [0] * (N + 1)
left = 0

while left < N and S[left] == '<':
    A[left + 1] = A[left] + 1
    left += 1

while left < N:
    mid = left + 1
    while mid < N and S[mid] == '>':
        mid += 1

    right = mid
    while right < N and S[right] == '<':
        right += 1

    for l in range(left, mid)[:: -1]:
        A[l] = max(A[l], A[l + 1] + 1)
    for r in range(mid + 1, right + 1):
        A[r] = max(A[r], A[r - 1] + 1)
    left = right

ans = sum(A)
print(ans)