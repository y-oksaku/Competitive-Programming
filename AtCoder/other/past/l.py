from collections import deque, defaultdict

N = int(input())
A = [None]
for _ in range(N):
    A.append(deque(map(int, input().split())))

canBattle = [[False] * (N + 1) for _ in range(N + 1)]

que = deque([])
for i, a in enumerate(A[1:], start=1):
    que.append((i, a.popleft(), 1))

day = 0
visited = defaultdict(lambda: False)
while que:
    fr, to, now = que.popleft()
    day = max(day, now)
    if canBattle[fr][to]:
        visited[(fr, to)] = True
        visited[(to, fr)] = True
        if A[fr]:
            que.append((fr, A[fr].popleft(), now + 1))
        if A[to]:
            que.append((to, A[to].popleft(), now + 1))
    else:
        canBattle[fr][to] = True
        canBattle[to][fr] = True

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if not visited[(i, j)]:
            print(-1)
            exit()

print(day)