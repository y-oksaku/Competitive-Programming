from collections import deque

import sys
input = sys.stdin.buffer.readline

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

dist = [10**10] * N
que = deque([(0, 0)])
while que:
    now, d = que.popleft()

    if dist[now] <= d:
        continue
    dist[now] = d

    for to in edges[now]:
        que.append((to, d + 1))

A = [i for i, d in enumerate(dist) if d % 2 == 0]
B = [i for i, d in enumerate(dist) if d % 2 == 1]

if len(A) > len(B):
    A, B = B, A

ans = [-1] * N
nums = set(range(1, N + 1))

if len(A) <= N // 3:
    mul = 1
    for i in A:
        ans[i] = 3 * mul
        nums.remove(3 * mul)
        mul += 1
    nums = list(nums)
    for i, n in zip(B, nums):
        ans[i] = n
else:
    mul = 1
    for c, i in enumerate(A):
        if c * 3 + 1 > N:
            ans[i] = mul * 3
            mul += 1
        else:
            ans[i] = c * 3 + 1
    for c, i in enumerate(B):
        if c * 3 + 2 > N:
            ans[i] = mul * 3
            mul += 1
        else:
            ans[i] = c * 3 + 2

print(*ans)
