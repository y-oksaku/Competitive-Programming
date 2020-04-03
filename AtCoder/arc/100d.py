from collections import deque
N = int(input())
A = list(map(int, input().split()))

L = [(10**18, 10**18, 10**18)] * (N + 1)
left = 0
right = 0
que = deque([])
for i, a in enumerate(A, start=1):
    right += a
    que.append(a)
    while len(que) > 1 and abs(right - left) > abs((right - que[0]) - (left + que[0])):
        q = que.popleft()
        left += q
        right -= q
    L[i] = (abs(left - right), left, right)

R = [(10**18, 10**18, 10**18)] * (N + 1)
left = 0
right = 0
que = deque([])
for i, a in enumerate(A[::-1], start=1):
    right += a
    que.append(a)
    while len(que) > 1 and abs(right - left) > abs((right - que[0]) - (left + que[0])):
        q = que.popleft()
        left += q
        right -= q
    R[i] = (abs(left - right), left, right)

R = R[::-1]

ans = 10**18
for mid in range(1, N):
    X = [L[mid + 1][1], L[mid + 1][2], R[mid + 1][1], R[mid + 1][2]]
    if min(X) == 0:
        continue
    ans = min(ans, max(X) - min(X))
print(ans)
