from collections import deque

N , M = map(int,input().split())

to = [[]] * M

for i in range(N) :
    u , v = list(map(int,input().split()))
    to[u].append(v)

S , T = map(int,input())

q = deque([S])

while q :
    now = q.popleft()



