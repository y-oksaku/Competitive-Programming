S = input()
N = len(S)

A = [0] * (N + 1)
now = 0
for i, s in enumerate(S, start=1):
    if s == '<':
        now += 1
    else:
        now = 0
    A[i] = now

B = [0] * (N + 1)
now = 0
for i, s in enumerate(S[::-1], start=1):
    if s == '>':
        now += 1
    else:
        now = 0
    B[i] = now
B = B[::-1]

ans = [10**18] * (N + 1)
for i in range(N + 1):
    ans[i] = max(A[i], B[i])
print(sum(ans))
