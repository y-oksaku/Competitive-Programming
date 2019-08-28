from collections import deque

N = int(input())

edge = [[] for _ in range(N)]
conect = [[i,0] for i in range(N)] # つながる頂点の数 ... 多い頂点に大きい数字を与える

for _ in range(N-1) :
    a , b = map(int,input().split())
    a -= 1
    b -= 1
    conect[a][1] += 1
    conect[b][1] += 1
    edge[a].append(b)
    edge[b].append(a)

c = list(map(int,input().split()))
c.sort()

net = lambda A : A[1]

conect.sort(key=net,reverse=True)

ans = [0] * N

for i in range(N) :
    ans[conect[i][0]] = c[i]

checked = [False] * N
length = 0

for c , check in enumerate(checked) :
    if check :
        continue

    stack = deque([c])

    while stack :
        current = stack.pop()

        if checked[current] :
            continue

        checked[current] = True
        for v in edge[current] :
            if not checked[v] :
                stack.append(v)
                length += min(ans[current] , ans[v])

print(length)

for a in ans :
    print(a,end=' ')

print('')