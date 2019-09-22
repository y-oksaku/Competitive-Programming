from collections import deque

N, K = map(int, input().split())
P = list(map(int, input().split()))

maxQ = deque([])
minQ = deque([])

for i in range(K):
    while maxQ:
        if P[maxQ[-1]] <= P[i]:
            maxQ.pop()
        else:
            break
    maxQ.append(i)
    if maxQ[0] == i - K:
        maxQ.popleft()

    while minQ:
        if P[minQ[-1]] >= P[i]:
            minQ.pop()
        else:
            break
    minQ.append(i)
    if minQ[0] == i - K:
        minQ.popleft()

ans = 1
hasSame = False
seq = 1
for i in range(1, K):
    if P[i - 1] < P[i]:
        seq += 1
    else:
        seq = 1
if seq >= K:
    hasSame = True

for left in range(N - K):
    right = left + K

    if P[right - 1] < P[right]:
        seq += 1
    else:
        seq = 1

    while maxQ:
        if P[maxQ[-1]] <= P[right]:
            maxQ.pop()
        else:
            break
    maxQ.append(right)
    if maxQ[0] == right - K:
        maxQ.popleft()

    if left == minQ[0] and right == maxQ[0]:
        pass
    else:
        if seq < K:
            ans += 1
        else:
            if not hasSame:
                hasSame = True
                ans += 1

    while minQ:
        if P[minQ[-1]] >= P[right]:
            minQ.pop()
        else:
            break
    minQ.append(right)
    if minQ[0] == right - K:
        minQ.popleft()

print(ans)