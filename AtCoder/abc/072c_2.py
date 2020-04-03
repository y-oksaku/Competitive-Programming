from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

ans = 0
for a in range(max(A) + 1):
    ans = max(ans, cnt[a - 1] + cnt[a] + cnt[a + 1])
print(ans)
