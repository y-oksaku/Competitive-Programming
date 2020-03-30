S = input()
N = len(S)
ans = [1] * (N)

for i in range(N - 2):
    if S[i] == 'L':
        continue
    if S[i + 1] == 'R':
        ans[i + 2] += ans[i]
        ans[i] = 0

for i in range(2, N)[:: -1]:
    if S[i] == 'R':
        continue
    if S[i - 1] == 'L':
        ans[i - 2] += ans[i]
        ans[i] = 0

print(*ans)