from collections import Counter

N = int(input())
S = [list(input()) for _ in range(N)]

cnt = Counter(S[0])
for s in S[1:]:
    for t, c in cnt.items():
        cnt[t] = min(c, s.count(t))

ans = []
for s, c in cnt.items():
    ans += [s] * c

ans.sort()
print(''.join(ans))