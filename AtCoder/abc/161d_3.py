from collections import deque

K = int(input())

que = deque([i for i in range(1, 10)])
ans = []
while len(ans) <= K + 10:
    now = que.popleft()
    ans.append(now)

    b = now % 10
    for i in range(max(0, b - 1), min(10, b + 2)):
        que.append(now * 10 + i)

ans.sort()
print(ans[K - 1])
