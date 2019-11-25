from collections import defaultdict, deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

cumA = [0] * (N + 1)
for i in range(1, N + 1):
    cumA[i] = cumA[i - 1] + A[i - 1]

cnt = defaultdict(int)
que = deque([])
ans = 0

for i, c in enumerate(cumA):
    while que and que[0][0] <= i - K:
        cnt[que.popleft()[1]] -= 1
    diff = (i - c) % K
    ans += cnt[diff]
    cnt[diff] += 1
    que.append((i, diff))
print(ans)