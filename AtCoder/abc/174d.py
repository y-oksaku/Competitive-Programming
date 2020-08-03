N = int(input())
C = list(input())

ans = 0
r = N - 1
for l in range(N):
    if C[l] == 'R':
        continue
    r = max(l, r)
    while r > l and C[r] == 'W':
        r -= 1
    if r <= l:
        break
    C[l], C[r] = C[r], C[l]
    ans += 1

print(ans)
