from collections import deque
import sys
input = sys.stdin.readline

N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for _ in range(N)]
XH.sort()

ans = 0
cnt = 0
que = deque()

for x, h in XH:
    while que and que[0][0] <= x:
        cnt -= que.popleft()[1]

    h -= cnt * A

    if h <= 0:
        continue

    ness = -(-h // A)
    cnt += ness
    ans += ness
    que.append((x + 2 * D + 1, ness))

print(ans)
