N, M = map(int, input().split())

W = [1] * (N + 1)
W[1] = 0
R = [0] * (N + 1)
R[1] = 1
cnt = [1] * (N + 1)

for _ in range(M):
    fr, to = map(int, input().split())
    cnt[fr] -= 1
    cnt[to] += 1

    if R[fr] == 1 and W[fr] >= 1:
        R[to] = 1
        W[to] += 1

    if R[fr] == 1 and W[fr] == 0:
        R[fr] = 0
        R[to] = 1

    if R[fr] == 0 and W[fr] >= 1:
        W[fr] -= 1
        W[to] += 1

    if cnt[fr] == 0:
        W[fr] = 0
        R[fr] = 0

ans = len([0 for r in R if r >= 1])
print(ans)
