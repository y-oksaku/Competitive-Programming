from collections import Counter
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

A = list(map(int, input().split()))
A.sort()
S = sum(A) - A[-1]

print(S)

ans = [0] * N
st = [(0, -1)]
while st:
    now, pr = st.pop()
    ans[now] = A.pop()
    for to in edges[now]:
        if to == pr:
            continue
        st.append((to, now))
print(*ans)
