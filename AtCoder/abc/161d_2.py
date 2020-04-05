from collections import deque
K = int(input())

que = deque(map(str, range(1, 10)))
while K > 1:
    n = que.popleft()
    K -= 1
    R = int(n[-1])
    for r in (R - 1, R, R + 1):
        if 0 <= r <= 9:
            que.append(n + str(r))

print(que[0])
