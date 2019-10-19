from collections import deque

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to, c = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append((to, c))
    edges[to].append((fr, c))

depth = [-1] * N
st = deque([(0, -1, 0)])  # now, parent, dep

while st:
    now, parent, d = st.pop()

    depth[now] = d

    for to, c in edges[now]:
        if to == parent:
            continue
        st.append((to, now, d + c))

ans = [d % 2 for d in depth]
print(*ans, sep='\n')