S = input()
T = set(list('AGCT'))

ans = 0
for l in range(len(S)):
    for r in range(l + 1, len(S) + 1):
        if set(S[l: r]) <= T:
            ans = max(ans, r - l)

print(ans)
