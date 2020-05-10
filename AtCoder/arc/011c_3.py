from collections import deque

start, end = input().split()
N = int(input())

S = set([input() for _ in range(N)])
S.add(start)
S.add(end)
S = list(S)
N = len(S)

edges = [[] for _ in range(N)]
startI, endI = S.index(start), S.index(end)

def canChange(S, T):
    ret = 0
    for s, t in zip(S, T):
        if s != t:
            ret += 1
        if ret > 1:
            return False
    return ret == 1

for i, s in enumerate(S):
    for j, t in enumerate(S[i + 1:], start=i + 1):
        if canChange(s, t):
            edges[i].append(j)
            edges[j].append(i)

parent = [None] * N
que = deque([startI])

while que:
    now = que.popleft()
    for to in edges[now]:
        if parent[to] == None:
            parent[to] = now
            que.append(to)

if parent[endI] == None:
    print('-1')
    exit()

ans = [S[endI]]
now = endI
while now != startI:
    now = parent[now]
    ans.append(S[now])
if len(ans) == 1:
    ans.append(ans[0])

print(len(ans) - 2)
print(*ans[::-1], sep='\n')
