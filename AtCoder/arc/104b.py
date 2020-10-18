from collections import Counter

_, S = input().split()
N = len(S)

ans = 0
for l in range(N):
    cnt = Counter()
    for i in range(l, N):
        cnt[S[i]] += 1
        if cnt['A'] == cnt['T'] and cnt['C'] == cnt['G']:
            ans += 1
print(ans)
