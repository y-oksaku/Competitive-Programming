N = int(input())
H = [int(input()) for _ in range(N)]

ans = [1] * N

mx = 0
left = 1
for i, h in enumerate(H, start=1):
    ans[i - 1] -= left
    if mx >= h:
        left = i
        mx = h
    else:
        mx = h

mx = 0
right = N
for i in range(N)[::-1]:
    h = H[i]
    if mx >= h:
        right = i + 1
        mx = h
    else:
        mx = h
    ans[i] += right

print(max(ans))
