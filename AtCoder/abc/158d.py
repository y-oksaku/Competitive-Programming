from collections import deque
import sys
input = sys.stdin.readline

S = input().rstrip()
Q = int(input())
FTC = [tuple(input().split()) for _ in range(Q)]

que = deque(['?'])
cnt = 0
for query in FTC:
    if query[0] == '1':
        cnt ^= 1
        continue

    sign = 0 if query[1] == '1' else 1

    if sign ^ cnt == 0:
        que.appendleft(query[2])
    else:
        que.append(query[2])

que = list(que)
ans = ''.join(que[:: (-1)**cnt])
ans = ans.replace('?', S[:: (-1)**cnt])

print(ans)