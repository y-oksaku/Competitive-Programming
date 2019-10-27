N, D, K = map(int, input().split())

LR = []
for _ in range(D):
    l, r = map(int, input().split())
    LR.append((l, r))

STA = []
STB = []
for i in range(K):
    s, t = map(int, input().split())
    if s < t:
        STA.append((i, s, t))
    else:
        STB.append((i, s, t))

ans = [D for _ in range(K)]

for day, (L, R) in enumerate(LR):
    for i, (num, S, T) in enumerate(STA):
        if L <= S:
            S = max(S, R)
            STA[i] = (num, S, T)
            if T <= S:
                ans[num] = min(ans[num], day + 1)

    for i, (num, S, T) in enumerate(STB):
        if S <= R:
            S = min(S, L)
            STB[i] = (num, S, T)
            if S <= T:
                ans[num] = min(ans[num], day + 1)

for day in ans:
    print(day)