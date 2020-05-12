from collections import deque, Counter
import string

N, K = map(int, input().split())
S = input()

def cntToTuple(cnt):
    return tuple([cnt[s] for s in string.ascii_lowercase])

cnt = Counter(list(S[:K]))
que = deque([cntToTuple(cnt)])
V = set()

for l, r in zip(S, S[K:]):
    if len(que) >= K:
        V.add(que.popleft())
    cnt[l] -= 1
    cnt[r] += 1
    T = cntToTuple(cnt)
    if T in V:
        print('YES')
        exit()
    que.append(T)

print('NO')