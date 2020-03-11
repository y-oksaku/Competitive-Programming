from collections import deque
import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

P = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    P[p - 1] += x

ans = [-1] * N
st = deque([(0, 0)])
while st:
    now, val = st.pop()

    if ans[now] >= 0:
        continue
    val += P[now]
    ans[now] = val

    for to in edges[now]:
        st.append((to, val))

print(*ans)
