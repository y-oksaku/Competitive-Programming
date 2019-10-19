N = int(input())
L = list(map(int, input().split()))
M = max(L)

cntL = [0] * (M + 1)
for l in L:
    cntL[l] += 1

accCntL = [0] * (M + 2)
for i in range(1, M + 2):
    accCntL[i] = accCntL[i - 1] + cntL[i - 1]

ans = 0
for i, A in enumerate(L):
    for j, B in enumerate(L):
        if i == j:
            continue

        right = min(A + B, M + 1)
        left = abs(A - B) + 1
        ans += accCntL[right] - accCntL[left]

        if left <= A < right:
            ans -= 1
        if left <= B < right:
            ans -= 1

print(ans // 6)
