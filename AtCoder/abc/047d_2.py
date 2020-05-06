N, T = map(int, input().split())
A = list(map(int, input().split()))

mx = [0] * (N + 1)
for i, a in enumerate(A[::-1], start=1):
    mx[-i] = max(mx[-i + 1], a)

mxD = 0
ans = 0
for i, a in enumerate(A):
    d = mx[i + 1] - a
    if mxD < d:
        mxD = d
        ans = 0
    if mxD == d:
        ans += 1

print(ans)
