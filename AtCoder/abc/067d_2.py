N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

def calc(s):
    st = [s]
    minDist = [10**18] * N
    minDist[s] = 0
    while st:
        now = st.pop()
        for to in edges[now]:
            if minDist[to] > minDist[now] + 1:
                minDist[to] = minDist[now] + 1
                st.append(to)
    return minDist

A = calc(0)
B = calc(N - 1)

ans = 0
for i in range(N):
    ans += 1 if A[i] <= B[i] else -1
print('Fennec' if ans > 0 else 'Snuke')
