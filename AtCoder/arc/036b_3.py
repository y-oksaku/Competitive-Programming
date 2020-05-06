N = int(input())
H = [int(input()) for _ in range(N)]

L = [0] * N
mx = H[0]
for i, h in enumerate(H):
    if mx < h:
        L[i] = L[i - 1] + 1
    mx = h

R = [0] * N
mx = H[-1]
for i, h in enumerate(H[::-1]):
    if mx < h:
        R[i] = R[i - 1] + 1
    mx = h
R = R[::-1]

ans = 0
for i in range(N):
    ans = max(ans, L[i] + R[i] + 1)
print(ans)
