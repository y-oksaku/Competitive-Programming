import string
from collections import deque

N, K = map(int, input().split())
S = input()

now = {s: 0 for s in string.ascii_lowercase}
for s in S[:K]:
    now[s] += 1

V = set()
que = deque([tuple([(s, now[s]) for s in string.ascii_lowercase])])
for l, r in zip(S, S[K:]):
    if len(que) >= K:
        V.add(que.popleft())

    now[l] -= 1
    now[r] += 1

    a = tuple([(s, now[s]) for s in string.ascii_lowercase])
    if a in V:
        print('YES')
        exit()
    que.append(a)

print('NO')